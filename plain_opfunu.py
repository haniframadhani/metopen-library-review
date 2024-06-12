from opfunu.cec_based.cec2013 import F12013
from opfunu.name_based import Ackley01
from opfunu import draw_2d, draw_3d

# func = F12013(ndim=2)
# result = func.evaluate(func.create_solution())

func = Ackley01(ndim=2)
result = func.evaluate(2)

# func.plot_2d(selected_dims=(2, 3), n_points=300, ct_cmap="viridis", ct_levels=30, ct_alpha=0.7,
#              fixed_strategy="mean", fixed_values=None, title="Contour map of the Ackley01 function",
#              x_label=None, y_label=None, figsize=(10, 8), filename="2d-Ackley01", exts=(".png", ".pdf"), verbose=True)
# draw_2d(func.evaluate, func.lb, func.ub,
#         selected_dims=(2, 3), n_points=300)
# func.plot_3d(selected_dims=(1, 6), n_points=500, ct_cmap="viridis", ct_levels=30, ct_alpha=0.7,
#              fixed_strategy="mean", fixed_values=None, title="3D visualization of the Ackley01 function",
#              x_label=None, y_label=None, figsize=(10, 8), filename="3d-Ackley01", exts=(".png", ".pdf"), verbose=True)
# draw_3d(func.evaluate, func.lb, func.ub,
#         selected_dims=(2, 3), n_points=300)

print(result)
