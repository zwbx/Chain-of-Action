# Chain-of-Action: Trajectory Autoregressive Modeling for Robotic Manipulation

🚧 **Code coming soon!** 🚧  
We're cleaning things up to make it clear, modular, and easy to use.

In the meantime, check out our:

- [📄 Paper on arXiv](https://arxiv.org/pdf/2506.09990)
- [🌐 Project Page](https://chain-of-action.github.io)

---

## 🔁 What is Chain-of-Action?

Chain-of-Action rethinks visuomotor policy learning by modeling action **trajectories from goal to start**, rather than predicting forward from the current state.

Unlike forward policies like ACT or Diffusion Policy, our model **starts from the final gripper pose** and autoregressively reasons backward—  
step by step, toward the current observation.

> ✅ No extra parameters  
> ✅ No extra data  
> ✅ Just a smarter modeling paradigm

This shift enables **strong spatial generalization** without tricks.

---

⭐️ **Stay tuned!**  
We're working on releasing a clean, modular implementation to make Chain-of-Action easy to use, extend, and build upon.  
Hit the star button if you’d like to follow along!
