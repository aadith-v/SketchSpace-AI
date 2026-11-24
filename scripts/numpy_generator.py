"""Pure NumPy UNet Generator forward pass for SketchSpace AI.
Enables offline CPU inference matching PyTorch UNetGenerator with bit-exact parity
for both Experiment 1 (ConvTranspose2d) and Experiment 2 (Nearest-Neighbor + Conv2d).
"""

import zipfile
import pickle
from pathlib import Path
import numpy as np
from PIL import Image
from numpy.lib.stride_tricks import as_strided

class TorchTensorLoader(pickle.Unpickler):
    def __init__(self, f, zip_ref, top):
        super().__init__(f)
        self.zip_ref = zip_ref
        self.top = top

    def persistent_load(self, pid):
        if isinstance(pid, tuple) and pid[0] == 'storage':
            raw = self.zip_ref.read(self.top + '/data/' + str(pid[2]))
            return np.frombuffer(raw, dtype=np.float32)
        return pid

    def find_class(self, module, name):
        if 'torch' in module:
            if '_rebuild_tensor_v2' in name:
                return lambda storage, storage_offset, size, stride, requires_grad, backward_hooks: storage[storage_offset:storage_offset+int(np.prod(size))].reshape(size)
            if '_rebuild_parameter' in name:
                return lambda data, requires_grad, backward_hooks: data
            return lambda *args, **kwargs: args
        return super().find_class(module, name)

def load_weights(ckpt_path):
    with zipfile.ZipFile(ckpt_path) as z:
        top = z.namelist()[0].split('/')[0]
        with z.open(top + '/data.pkl') as f:
            data = TorchTensorLoader(f, z, top).load()
            return data['generator_state_dict']

def conv2d(x, w, b=None, s=1, p=0):
    C, H, W = x.shape
    out_c, in_c, kh, kw = w.shape
    if p > 0:
        x = np.pad(x, ((0,0), (p,p), (p,p)), mode='constant')
        H += 2 * p
        W += 2 * p
    out_h = (H - kh) // s + 1
    out_w = (W - kw) // s + 1
    shape = (C, kh, kw, out_h, out_w)
    strides = (x.strides[0], x.strides[1], x.strides[2], s * x.strides[1], s * x.strides[2])
    cols = as_strided(x, shape=shape, strides=strides)
    cols = cols.transpose(3, 4, 0, 1, 2).reshape(out_h * out_w, C * kh * kw)
    out = np.dot(cols, w.reshape(out_c, -1).T)
    if b is not None:
        out += b
    return out.reshape(out_h, out_w, out_c).transpose(2, 0, 1)

def conv_transpose2d(x, w, b=None, s=2, p=1):
    in_c, H, W = x.shape
    _, out_c, kh, kw = w.shape
    out_h = H * s
    out_w = W * s
    pad_h = out_h + 2 * p
    pad_w = out_w + 2 * p
    out = np.zeros((out_c, pad_h, pad_w), dtype=np.float32)
    x_flat = x.reshape(in_c, -1)
    for di in range(kh):
        for dj in range(kw):
            w_slice = w[:, :, di, dj]
            term = np.dot(w_slice.T, x_flat).reshape(out_c, H, W)
            out[:, di:di + H*s:s, dj:dj + W*s:s] += term
    out = out[:, p:p + out_h, p:p + out_w]
    if b is not None:
        out += b[:, None, None]
    return out

def bn(x, mean, var, weight, bias, eps=1e-5):
    inv_std = 1.0 / np.sqrt(var + eps)
    return ((x - mean[:, None, None]) * inv_std[:, None, None]) * weight[:, None, None] + bias[:, None, None]

def lrelu(x):
    return np.where(x > 0, x, x * 0.2)

def relu(x):
    return np.maximum(x, 0)

def upsample_nearest(x):
    return np.repeat(np.repeat(x, 2, axis=1), 2, axis=2)

class NumpyUNet:
    def __init__(self, ckpt_path):
        self.w = load_weights(ckpt_path)
        # detect mode
        if any('.conv.weight' in k or '.3.1.weight' in k for k in self.w.keys()):
            self.mode = 'nearest'
        else:
            self.mode = 'deconv'

    def forward(self, img_np_norm):
        if self.mode == 'nearest':
            return self.forward_nearest(img_np_norm)
        else:
            return self.forward_deconv(img_np_norm)

    def forward_nearest(self, img_np_norm):
        w = self.w
        # --- ENCODER ---
        d1 = conv2d(img_np_norm, w['model.model.0.weight'], s=2, p=1) # (32, 128, 128)

        d2 = conv2d(lrelu(d1), w['model.model.1.model.1.weight'], s=2, p=1)
        d2 = bn(d2, w['model.model.1.model.2.running_mean'], w['model.model.1.model.2.running_var'],
                w['model.model.1.model.2.weight'], w['model.model.1.model.2.bias'])

        d3 = conv2d(lrelu(d2), w['model.model.1.model.3.model.1.weight'], s=2, p=1)
        d3 = bn(d3, w['model.model.1.model.3.model.2.running_mean'], w['model.model.1.model.3.model.2.running_var'],
                w['model.model.1.model.3.model.2.weight'], w['model.model.1.model.3.model.2.bias'])

        d4 = conv2d(lrelu(d3), w['model.model.1.model.3.model.3.model.1.weight'], s=2, p=1)
        d4 = bn(d4, w['model.model.1.model.3.model.3.model.2.running_mean'], w['model.model.1.model.3.model.3.model.2.running_var'],
                w['model.model.1.model.3.model.3.model.2.weight'], w['model.model.1.model.3.model.3.model.2.bias'])

        d5 = conv2d(lrelu(d4), w['model.model.1.model.3.model.3.model.3.model.1.weight'], s=2, p=1)
        d5 = bn(d5, w['model.model.1.model.3.model.3.model.3.model.2.running_mean'], w['model.model.1.model.3.model.3.model.3.model.2.running_var'],
                w['model.model.1.model.3.model.3.model.3.model.2.weight'], w['model.model.1.model.3.model.3.model.3.model.2.bias'])

        d6 = conv2d(lrelu(d5), w['model.model.1.model.3.model.3.model.3.model.3.model.1.weight'], s=2, p=1)
        d6 = bn(d6, w['model.model.1.model.3.model.3.model.3.model.3.model.2.running_mean'], w['model.model.1.model.3.model.3.model.3.model.3.model.2.running_var'],
                w['model.model.1.model.3.model.3.model.3.model.3.model.2.weight'], w['model.model.1.model.3.model.3.model.3.model.3.model.2.bias'])

        d7 = conv2d(lrelu(d6), w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.1.weight'], s=2, p=1)
        d7 = bn(d7, w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.2.running_mean'], w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.2.running_var'],
                w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.2.weight'], w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.2.bias'])

        d8 = conv2d(lrelu(d7), w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.3.model.1.weight'], s=2, p=1)

        # --- DECODER ---
        u8 = relu(d8)
        u8 = upsample_nearest(u8)
        u8 = conv2d(u8, w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.3.model.3.1.weight'], s=1, p=1)
        u8 = bn(u8, w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.3.model.4.running_mean'],
                    w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.3.model.4.running_var'],
                    w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.3.model.4.weight'],
                    w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.3.model.4.bias'])
        c7 = np.concatenate([d7, u8], axis=0)

        u7 = relu(c7)
        u7 = upsample_nearest(u7)
        u7 = conv2d(u7, w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.5.1.weight'], s=1, p=1)
        u7 = bn(u7, w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.6.running_mean'],
                    w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.6.running_var'],
                    w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.6.weight'],
                    w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.6.bias'])
        c6 = np.concatenate([d6, u7], axis=0)

        u6 = relu(c6)
        u6 = upsample_nearest(u6)
        u6 = conv2d(u6, w['model.model.1.model.3.model.3.model.3.model.3.model.5.1.weight'], s=1, p=1)
        u6 = bn(u6, w['model.model.1.model.3.model.3.model.3.model.3.model.6.running_mean'],
                    w['model.model.1.model.3.model.3.model.3.model.3.model.6.running_var'],
                    w['model.model.1.model.3.model.3.model.3.model.3.model.6.weight'],
                    w['model.model.1.model.3.model.3.model.3.model.3.model.6.bias'])
        c5 = np.concatenate([d5, u6], axis=0)

        u5 = relu(c5)
        u5 = upsample_nearest(u5)
        u5 = conv2d(u5, w['model.model.1.model.3.model.3.model.3.model.5.1.weight'], s=1, p=1)
        u5 = bn(u5, w['model.model.1.model.3.model.3.model.3.model.6.running_mean'],
                    w['model.model.1.model.3.model.3.model.3.model.6.running_var'],
                    w['model.model.1.model.3.model.3.model.3.model.6.weight'],
                    w['model.model.1.model.3.model.3.model.3.model.6.bias'])
        c4 = np.concatenate([d4, u5], axis=0)

        u4 = relu(c4)
        u4 = upsample_nearest(u4)
        u4 = conv2d(u4, w['model.model.1.model.3.model.3.model.5.1.weight'], s=1, p=1)
        u4 = bn(u4, w['model.model.1.model.3.model.3.model.6.running_mean'],
                    w['model.model.1.model.3.model.3.model.6.running_var'],
                    w['model.model.1.model.3.model.3.model.6.weight'],
                    w['model.model.1.model.3.model.3.model.6.bias'])
        c3 = np.concatenate([d3, u4], axis=0)

        u3 = relu(c3)
        u3 = upsample_nearest(u3)
        u3 = conv2d(u3, w['model.model.1.model.3.model.5.1.weight'], s=1, p=1)
        u3 = bn(u3, w['model.model.1.model.3.model.6.running_mean'],
                    w['model.model.1.model.3.model.6.running_var'],
                    w['model.model.1.model.3.model.6.weight'],
                    w['model.model.1.model.3.model.6.bias'])
        c2 = np.concatenate([d2, u3], axis=0)

        u2 = relu(c2)
        u2 = upsample_nearest(u2)
        u2 = conv2d(u2, w['model.model.1.model.5.1.weight'], s=1, p=1)
        u2 = bn(u2, w['model.model.1.model.6.running_mean'],
                    w['model.model.1.model.6.running_var'],
                    w['model.model.1.model.6.weight'],
                    w['model.model.1.model.6.bias'])
        c1 = np.concatenate([d1, u2], axis=0)

        u1 = relu(c1)
        u1 = upsample_nearest(u1)
        u1 = conv2d(u1, w['model.model.3.1.weight'], b=w['model.model.3.1.bias'], s=1, p=1)
        out = np.tanh(u1)
        return out

    def forward_deconv(self, img_np_norm):
        w = self.w
        # --- ENCODER ---
        d1 = conv2d(img_np_norm, w['model.model.0.weight'], s=2, p=1) # (32, 128, 128)

        d2 = conv2d(lrelu(d1), w['model.model.1.model.1.weight'], s=2, p=1)
        d2 = bn(d2, w['model.model.1.model.2.running_mean'], w['model.model.1.model.2.running_var'],
                w['model.model.1.model.2.weight'], w['model.model.1.model.2.bias'])

        d3 = conv2d(lrelu(d2), w['model.model.1.model.3.model.1.weight'], s=2, p=1)
        d3 = bn(d3, w['model.model.1.model.3.model.2.running_mean'], w['model.model.1.model.3.model.2.running_var'],
                w['model.model.1.model.3.model.2.weight'], w['model.model.1.model.3.model.2.bias'])

        d4 = conv2d(lrelu(d3), w['model.model.1.model.3.model.3.model.1.weight'], s=2, p=1)
        d4 = bn(d4, w['model.model.1.model.3.model.3.model.2.running_mean'], w['model.model.1.model.3.model.3.model.2.running_var'],
                w['model.model.1.model.3.model.3.model.2.weight'], w['model.model.1.model.3.model.3.model.2.bias'])

        d5 = conv2d(lrelu(d4), w['model.model.1.model.3.model.3.model.3.model.1.weight'], s=2, p=1)
        d5 = bn(d5, w['model.model.1.model.3.model.3.model.3.model.2.running_mean'], w['model.model.1.model.3.model.3.model.3.model.2.running_var'],
                w['model.model.1.model.3.model.3.model.3.model.2.weight'], w['model.model.1.model.3.model.3.model.3.model.2.bias'])

        d6 = conv2d(lrelu(d5), w['model.model.1.model.3.model.3.model.3.model.3.model.1.weight'], s=2, p=1)
        d6 = bn(d6, w['model.model.1.model.3.model.3.model.3.model.3.model.2.running_mean'], w['model.model.1.model.3.model.3.model.3.model.3.model.2.running_var'],
                w['model.model.1.model.3.model.3.model.3.model.3.model.2.weight'], w['model.model.1.model.3.model.3.model.3.model.3.model.2.bias'])

        d7 = conv2d(lrelu(d6), w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.1.weight'], s=2, p=1)
        d7 = bn(d7, w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.2.running_mean'], w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.2.running_var'],
                w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.2.weight'], w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.2.bias'])

        d8 = conv2d(lrelu(d7), w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.3.model.1.weight'], s=2, p=1)

        # --- DECODER with ConvTranspose2d ---
        u8 = relu(d8)
        u8 = conv_transpose2d(u8, w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.3.model.3.weight'], s=2, p=1)
        u8 = bn(u8, w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.3.model.4.running_mean'],
                    w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.3.model.4.running_var'],
                    w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.3.model.4.weight'],
                    w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.3.model.4.bias'])
        c7 = np.concatenate([d7, u8], axis=0)

        u7 = relu(c7)
        u7 = conv_transpose2d(u7, w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.5.weight'], s=2, p=1)
        u7 = bn(u7, w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.6.running_mean'],
                    w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.6.running_var'],
                    w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.6.weight'],
                    w['model.model.1.model.3.model.3.model.3.model.3.model.3.model.6.bias'])
        c6 = np.concatenate([d6, u7], axis=0)

        u6 = relu(c6)
        u6 = conv_transpose2d(u6, w['model.model.1.model.3.model.3.model.3.model.3.model.5.weight'], s=2, p=1)
        u6 = bn(u6, w['model.model.1.model.3.model.3.model.3.model.3.model.6.running_mean'],
                    w['model.model.1.model.3.model.3.model.3.model.3.model.6.running_var'],
                    w['model.model.1.model.3.model.3.model.3.model.3.model.6.weight'],
                    w['model.model.1.model.3.model.3.model.3.model.3.model.6.bias'])
        c5 = np.concatenate([d5, u6], axis=0)

        u5 = relu(c5)
        u5 = conv_transpose2d(u5, w['model.model.1.model.3.model.3.model.3.model.5.weight'], s=2, p=1)
        u5 = bn(u5, w['model.model.1.model.3.model.3.model.3.model.6.running_mean'],
                    w['model.model.1.model.3.model.3.model.3.model.6.running_var'],
                    w['model.model.1.model.3.model.3.model.3.model.6.weight'],
                    w['model.model.1.model.3.model.3.model.3.model.6.bias'])
        c4 = np.concatenate([d4, u5], axis=0)

        u4 = relu(c4)
        u4 = conv_transpose2d(u4, w['model.model.1.model.3.model.3.model.5.weight'], s=2, p=1)
        u4 = bn(u4, w['model.model.1.model.3.model.3.model.6.running_mean'],
                    w['model.model.1.model.3.model.3.model.6.running_var'],
                    w['model.model.1.model.3.model.3.model.6.weight'],
                    w['model.model.1.model.3.model.3.model.6.bias'])
        c3 = np.concatenate([d3, u4], axis=0)

        u3 = relu(c3)
        u3 = conv_transpose2d(u3, w['model.model.1.model.3.model.5.weight'], s=2, p=1)
        u3 = bn(u3, w['model.model.1.model.3.model.6.running_mean'],
                    w['model.model.1.model.3.model.6.running_var'],
                    w['model.model.1.model.3.model.6.weight'],
                    w['model.model.1.model.3.model.6.bias'])
        c2 = np.concatenate([d2, u3], axis=0)

        u2 = relu(c2)
        u2 = conv_transpose2d(u2, w['model.model.1.model.5.weight'], s=2, p=1)
        u2 = bn(u2, w['model.model.1.model.6.running_mean'],
                    w['model.model.1.model.6.running_var'],
                    w['model.model.1.model.6.weight'],
                    w['model.model.1.model.6.bias'])
        c1 = np.concatenate([d1, u2], axis=0)

        u1 = relu(c1)
        u1 = conv_transpose2d(u1, w['model.model.3.weight'], b=w['model.model.3.bias'], s=2, p=1)
        out = np.tanh(u1)
        return out
