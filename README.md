# aiera-api-examples

Documentation for Aiera's API is available at: [https://rest.aiera.com/](https://rest.aiera.com/)  


This repository contains code examples for interacting with Aiera's APIs. To set up the environment using [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) use the environment described in the repository's `environment.yml` file:

```bash
conda env create -f environment.yml

# activate the environment
conda activate aiera-api-examples
```

To use the examples, you will also need to set your API key as an evironment variable:

```bash
export AIERA_API_KEY=...
```


## Collecting sentiment via monitor api

The example in `examples/monitor_sentiment.py` shows how someone would pull all sentiment values for all events associated with a monitor. Additional processing can be executed based on the schemas in our [monitor api](https://rest.aiera.com/docs/monitor-matches) and our [events api](https://rest.aiera.com/docs/get-event).


```bash
python examples/monitor_sentiment.py
```
