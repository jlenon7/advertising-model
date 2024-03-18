# Advertising Model 🤖

> Model that predicts how many sales has been made according to the number of advertisements in each channel.

[![GitHub followers](https://img.shields.io/github/followers/jlenon7.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/jlenon7?tab=followers)
[![GitHub stars](https://img.shields.io/github/stars/jlenon7/advertising-model.svg?style=social&label=Star&maxAge=2592000)](https://github.com/jlenon7/advertising-model/stargazers/)

<p>
    <a href="https://www.buymeacoffee.com/athenna" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
</p>

## Results

The model needs more training to be more precise:

<img src="resources/predictions.png" width="500px">
<img src="resources/mae-mse-rmse.png" width="500px">

## Running

To run the model first create a new Python environment and activate it. I'm using [Anaconda](https://www.anaconda.com/) for that:

```shell
conda create -n advertising_env python=3.11
conda activate advertising_env
```

Now install all the project dependencies:

```shell
make install-all
```

And run the model:

```shell
make model
```
