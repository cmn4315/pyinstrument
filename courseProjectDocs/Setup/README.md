# To Reproduce testResults and testCoverage:

1. Follow the instructions from the main project README to set up a dev environment:

    ```
        virtualenv --python=python3 env
        . env/bin/activate
        pip install --upgrade pip
        pip install -r requirements-dev.txt
        prek install --install-hooks
    ```

2. Install pytest-cov:

    ```
        pip install pytest-cov
    ```

3. Run pytest-cov on the pyinstrument project:

    ```
        pytest --cov=pyinstrument test/
    ```
