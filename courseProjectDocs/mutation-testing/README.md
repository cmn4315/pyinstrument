# To Reproduct Mutation Testing:

1. Follow the instructions from the main project README to set up a dev environment:

    ```
        virtualenv --python=python3 env
        . env/bin/activate
        pip install --upgrade pip
        pip install -r requirements-dev.txt
        prek install --install-hooks
    ```

2. Install mutmut

    ```
        pip install mutmut
    ```

3. Run mutmut

    ```
        mutmut run
    ```

4. View mutmut Results

    ```
        mutmut browse
    ```
