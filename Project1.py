{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Project 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy import stats\n",
    "import numpy as np\n",
    "import pandas as pd \n",
    "import matplotlib\n",
    "import matplotlib.pyplot as plt\n",
    "import math\n",
    "from sklearn.linear_model import Lasso\n",
    "from sklearn.linear_model import LinearRegression"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "http://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CRIM</th>\n",
       "      <th>ZN</th>\n",
       "      <th>INDUS</th>\n",
       "      <th>CHAS</th>\n",
       "      <th>NOX</th>\n",
       "      <th>RM</th>\n",
       "      <th>AGE</th>\n",
       "      <th>DIS</th>\n",
       "      <th>RAD</th>\n",
       "      <th>TAX</th>\n",
       "      <th>PTRATIO</th>\n",
       "      <th>B</th>\n",
       "      <th>LSTAT</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.00632</td>\n",
       "      <td>18.0</td>\n",
       "      <td>2.31</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.538</td>\n",
       "      <td>6.575</td>\n",
       "      <td>65.2</td>\n",
       "      <td>4.0900</td>\n",
       "      <td>1.0</td>\n",
       "      <td>296.0</td>\n",
       "      <td>15.3</td>\n",
       "      <td>396.90</td>\n",
       "      <td>4.98</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.02731</td>\n",
       "      <td>0.0</td>\n",
       "      <td>7.07</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.469</td>\n",
       "      <td>6.421</td>\n",
       "      <td>78.9</td>\n",
       "      <td>4.9671</td>\n",
       "      <td>2.0</td>\n",
       "      <td>242.0</td>\n",
       "      <td>17.8</td>\n",
       "      <td>396.90</td>\n",
       "      <td>9.14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.02729</td>\n",
       "      <td>0.0</td>\n",
       "      <td>7.07</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.469</td>\n",
       "      <td>7.185</td>\n",
       "      <td>61.1</td>\n",
       "      <td>4.9671</td>\n",
       "      <td>2.0</td>\n",
       "      <td>242.0</td>\n",
       "      <td>17.8</td>\n",
       "      <td>392.83</td>\n",
       "      <td>4.03</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      CRIM    ZN  INDUS  CHAS    NOX     RM   AGE     DIS  RAD    TAX  \\\n",
       "0  0.00632  18.0   2.31   0.0  0.538  6.575  65.2  4.0900  1.0  296.0   \n",
       "1  0.02731   0.0   7.07   0.0  0.469  6.421  78.9  4.9671  2.0  242.0   \n",
       "2  0.02729   0.0   7.07   0.0  0.469  7.185  61.1  4.9671  2.0  242.0   \n",
       "\n",
       "   PTRATIO       B  LSTAT  \n",
       "0     15.3  396.90   4.98  \n",
       "1     17.8  396.90   9.14  \n",
       "2     17.8  392.83   4.03  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.datasets import load_boston\n",
    "data_set = load_boston()\n",
    "data_set_df = pd.DataFrame(data_set.data, columns=data_set.feature_names)\n",
    "data_set_df.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
