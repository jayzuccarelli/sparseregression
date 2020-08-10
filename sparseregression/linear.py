import pyomo.environ as pe


def sparse_linear_regression(X, y, k, engine='ipopt', executable='~', verbose=False):
    n, p = X.shape
    M = 1000

    # Create model
    m = pe.ConcreteModel()

    # Add variables
    m.beta = pe.Var(range(p))
    m.z = pe.Var(range(p), within=pe.Binary)

    # Add constraints
    def M1(m, j):
        return m.beta[j] <= M * m.z[j]

    m.bigm1 = pe.Constraint(range(p), rule=M1)

    def M2(m, j):
        return m.beta[j] >= -M * m.z[j]
    m.bigm2 = pe.Constraint(range(p), rule=M2)

    m.sparsity = pe.Constraint(expr=sum(m.z[j] for j in range(p)) <= k)

    # Add objective
    m.obj = pe.Objective(sense=pe.minimize, expr=sum(
        pow(y[i] - sum(X[i, j] * m.beta[j] for j in range(p)), 2)
        for i in range(n)))

    solver = pe.SolverFactory(engine, executable=executable)

    results = solver.solve(m, tee=verbose)
    return results, [m.beta[j].value for j in range(p)]
