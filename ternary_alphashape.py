import ternary
import alphashape
import matplotlib.pyplot as plt
from descartes import PolygonPatch


def to_t_points(points, permutation=None):
    """
    Transfer the points to the points which can be plot correctly on a ternary ax
    :param points: A list of 3-tuples that (i, j, k) requires i + j + k = scale
    :param permutation: string, None, equivalent to "012".
            The order of the coordinates, counterclockwise from the origin
    :return:
    """
    return [ternary.helpers.project_point(p, permutation=permutation) for p in points]


def add_alphashap(points, ax, alpha_value=None, alpha=0.3, fc=None, ec=None):
    """
    Add a alpha shape which corresponds to the ternary scatter plot
    :param points: A list of 3-tuples that (i, j, k) requires i + j + k = scale
    :param ax: the ax to plot the alpha shape, supposed to be same as the scatter plot
    :param alpha_value: float. default None which will calculate the optimize. If zero a Convex hill will be added
    :param alpha: float 0 to 1
    :param fc: fill color
    :param ec: edge color
    :return: None
    """
    t_points = to_t_points(points)
    if alpha_value is None:
        alpha_value = alphashape.optimizealpha(t_points)
    alpha_shape = alphashape.alphashape(t_points, alpha_value)
    ax.add_patch(PolygonPatch(alpha_shape, alpha=alpha, fc=fc, ec=ec))
