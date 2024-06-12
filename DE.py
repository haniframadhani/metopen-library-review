import sys
import numpy as np
from numpy.random import rand
from numpy.random import choice
from matplotlib import pyplot


class DE:
    def __init__(self, population_size: int, bounds: list, iter: int, F: float, cr: float):
        self.population_size = population_size
        self.bounds = bounds
        self.iter = iter
        self.F = F
        self.cr = cr

    def obj(self, x):
        # print(x[0]**2.0 + x[1]**2.0)
        # sys.exit()
        return x[0]**2.0 + x[1]**2.0

    def mutation(self, x, F):
        return x[0] + F * (x[1]-x[2])

    def check_bounds(self, mutated, bounds) -> list:
        mutated_bound = [np.clip(mutated[i], bounds[i, 0], bounds[i, 1])
                         for i in range(len(bounds))]
        return mutated_bound

    def crossover(self, mutated, target, dims, cr) -> list:
        p = rand(dims)
        trial = [mutated[i] if p[i] < cr else target[i] for i in range(dims)]
        return trial

    def main(self):
        pop = self.bounds[:, 0] + \
            (rand(self.population_size, len(self.bounds))
             * (self.bounds[:, 1]-self.bounds[:, 0]))
        obj_all = [self.obj(ind) for ind in pop]
        best_vector = pop[np.argmin(obj_all)]
        best_obj = min(obj_all)
        prev_obj = best_obj

        for i in range(self.iter):
            for j in range(self.population_size):
                candidates = [candidate for candidate in range(
                    self.population_size) if candidate != j]
                a, b, c = pop[choice(candidates, 3, replace=False)]
                mutated = self.mutation([a, b, c], self.F)
                mutated = self.check_bounds(mutated, self.bounds)
                trial = self.crossover(
                    mutated, pop[j], len(self.bounds), self.cr)
                obj_target = self.obj(pop[j])
                # print(obj_target)
                # sys.exit()
                obj_trial = self.obj(trial)
                # print(obj_trial)
                # sys.exit()
                if obj_trial < obj_target:
                    pop[j] = trial
                    obj_all[j] = obj_trial
            best_obj = np.min(obj_all)
            if best_obj < prev_obj:
                best_vector = pop[np.argmin(obj_all)]
                prev_obj = best_obj
                print('iteration: %d f([%s]) = %.5f' %
                      (i, np.around(best_vector, decimals=5), best_obj))
        return [best_vector, best_obj]


population_size = 10
bounds = np.asarray([(-5.0, 5.0), (-5.0, 5.0)])
iter = 100
F = 0.5
cr = 0.7

sol = DE(population_size, bounds, iter, F, cr)
solution = sol.main()
print('\nsolution: f([%s]) = %.5f' %
      (np.around(solution[0], decimals=5), solution[1]))
# pyplot.plot(solution[2], '.-')
# pyplot.xlabel('Improvement Number')
# pyplot.ylabel('Evaluation f(x)')
# pyplot.show()
