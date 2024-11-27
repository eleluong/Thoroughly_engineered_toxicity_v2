import concurrent.futures


def execute_multithreading_functions(functions):
    results = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for function in functions:
            results.append(executor.submit(function["fn"], **function["args"]))

    return [result.result() for result in results]
