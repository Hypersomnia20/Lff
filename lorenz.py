# Lff
洛伦兹力
import numpy as np
   import matplotlib.pyplot as plt
   from mpl_toolkits.mplot3d import Axes3D

   # 参数设置
   sigma, rho, beta = 10, 28, 8/3
   dt = 0.01
   steps = 5000

   # 洛伦兹方程
   def lorenz(x):
       return np.array([
           sigma*(x[1] - x[0]),
           x[0]*(rho - x[2]) - x[1],
           x[0]*x[1] - beta*x[2]]
       )

   # 计算轨迹
   x = np.array([1.0, 1.0, 1.0])
   traj = [x.copy()]
   for _ in range(steps):
       x += dt * lorenz(x)
       traj.append(x.copy())
   traj = np.array(traj)

   # 3D可视化
   fig = plt.figure(figsize=(10, 10))
   ax = fig.add_subplot(111, projection='3d')
   ax.plot(traj[:,0], traj[:,1], traj[:,2], lw=0.5, color='#FF69B4')
   
   # 美化设置
   ax.set_axis_off()  # 隐藏坐标轴
   ax.set_facecolor('black')  # 背景设为黑色
   plt.savefig('lorenz.png', dpi=300, bbox_inches='tight', pad_inches=0)
