{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "european_options_class.ipynb",
      "version": "0.3.2",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/TALeonard/19ma573thomasleonard/blob/master/src/european_options_class.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "metadata": {
        "id": "ypYrNOWxVwgE",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "class VanillaOption:\n",
        "    def __init__(\n",
        "        self,\n",
        "        otype = 1, # 1: 'call'\n",
        "                  # -1: 'put'\n",
        "        strike = 110.,\n",
        "        maturity = 1.,\n",
        "        market_price = 10.):\n",
        "      self.otype = otype\n",
        "      self.strike = strike\n",
        "      self.maturity = maturity\n",
        "      self.market_price = market_price #this will be used for calibration\n",
        "      \n",
        "        \n",
        "    def payoff(self, s): #s: excercise price\n",
        "      otype = self.otype\n",
        "      k = self.strike\n",
        "      maturity = self.maturity\n",
        "      return np.max([0, (s - k)*otype])"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}