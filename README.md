# Notice:
The **Chain-of-Action** repository has been transferred to [ByteDance-Seed/Chain-of-Action](https://github.com/ByteDance-Seed/Chain-of-Action).

---

# Chain-of-Action: Trajectory Autoregressive Modeling for Robotic Manipulation

- [📄 Paper on arXiv](https://arxiv.org/pdf/2506.09990)
- [🌐 Project Page](https://chain-of-action.github.io)

## 🔁 What is Chain-of-Action?

Chain-of-Action rethinks visuomotor policy learning by modeling action **trajectories from goal to start**, rather than predicting forward from the current state.

Unlike forward policies like ACT or Diffusion Policy, our model **starts from the final gripper pose** and autoregressively reasons backward—  
step by step, toward the current observation.

> ✅ No extra parameters  
> ✅ No extra data  
> ✅ Just a smarter modeling paradigm

This shift enables **strong spatial generalization** without tricks.
