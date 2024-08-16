import math
import matplotlib.pyplot as plt


class Gaussian:
    """
    Gaussian distribution class for calculating and visualizing a Gaussian distribution.
    Attributes:
                mean (float) representing the mean value of the distribution,
                stdev (float) representing the standard deviation of the distribution,
                data_list (list of floats) a list of floats extracted from the data file,

    """

    def __init__(self, mu=0, sigma=1):
        self.mean = mu
        self.stdev = sigma
        self.data = []

    def calculate_mean(self):
        """
        Method to calculate the mean of the data set.
        Args:
            None
        :return:
            float: mean of the data set
        """
        self.mean = sum(self.data) / len(self.data)
        return self.mean

    def calculate_stdev(self, sample=True):
        """
        Method to calculate the standard deviation of the data set.
        :param sample:
                whether the data represents a sample(sample == true) or population (sample == false)
        :return:
            float: standard deviation of the data set
        """
        # s = √[(Σ(xi - x̄)²) / (n - 1)] -> Population
        # σ = √[(Σ(xi - μ)²) / n]       -> Data sample
        if sample:
            sample_size = len(self.data) - 1
        else:
            sample_size = len(self.data)
        mean = self.mean
        deviation = 0
        for data in self.data:
            deviation += ((data - mean) ** 2)

        deviation = math.sqrt(deviation / sample_size)
        self.stdev = deviation
        return self.stdev


#                 "    def read_data_file(self, file_name, sample=True):\n",
#                 "    \n",
#                 "        \"\"\"Method to read in data from a txt file. The txt file should have\n",
#                 "        one number (float) per line. The numbers are stored in the data attribute. \n",
#                 "        After reading in the file, the mean and standard deviation are calculated\n",
#                 "                \n",
#                 "        Args:\n",
#                 "            file_name (string): name of a file to read from\n",
#                 "        \n",
#                 "        Returns:\n",
#                 "            None\n",
#                 "        \n",
#                 "        \"\"\"\n",
#                 "        \n",
#                 "        # This code opens a data file and appends the data to a list called data_list\n",
#                 "        with open(file_name) as file:\n",
#                 "            data_list = []\n",
#                 "            line = file.readline()\n",
#                 "            while line:\n",
#                 "                data_list.append(int(line))\n",
#                 "                line = file.readline()\n",
#                 "        file.close()\n",
#                 "    \n",
#                 "        # TODO: \n",
#                 "        #   Update the self.data attribute with the data_list\n",
#                 "        #   Update self.mean with the mean of the data_list. \n",
#                 "        #       You can use the calculate_mean() method with self.calculate_mean()\n",
#                 "        #   Update self.stdev with the standard deviation of the data_list. Use the \n",
#                 "        #       calcaulte_stdev() method.\n",
#                 "                \n",
#                 "        \n",
#                 "    def plot_histogram(self):\n",
#                 "        \"\"\"Method to output a histogram of the instance variable data using \n",
#                 "        matplotlib pyplot library.\n",
#                 "        \n",
#                 "        Args:\n",
#                 "            None\n",
#                 "            \n",
#                 "        Returns:\n",
#                 "            None\n",
#                 "        \"\"\"\n",
#                 "        \n",
#                 "        # TODO: Plot a histogram of the data_list using the matplotlib package.\n",
#                 "        #       Be sure to label the x and y axes and also give the chart a title\n",
#                 "        \n",
#                 "                \n",
#                 "        \n",
#                 "    def pdf(self, x):\n",
#                 "        \"\"\"Probability density function calculator for the gaussian distribution.\n",
#                 "        \n",
#                 "        Args:\n",
#                 "            x (float): point for calculating the probability density function\n",
#                 "            \n",
#                 "        \n",
#                 "        Returns:\n",
#                 "            float: probability density function output\n",
#                 "        \"\"\"\n",
#                 "        \n",
#                 "        # TODO: Calculate the probability density function of the Gaussian distribution\n",
#                 "        #       at the value x. You'll need to use self.stdev and self.mean to do the calculation\n",
#                 "        pass        \n",
#                 "\n",
#                 "    def plot_histogram_pdf(self, n_spaces = 50):\n",
#                 "\n",
#                 "        \"\"\"Method to plot the normalized histogram of the data and a plot of the \n",
#                 "        probability density function along the same range\n",
#                 "        \n",
#                 "        Args:\n",
#                 "            n_spaces (int): number of data points \n",
#                 "        \n",
#                 "        Returns:\n",
#                 "            list: x values for the pdf plot\n",
#                 "            list: y values for the pdf plot\n",
#                 "            \n",
#                 "        \"\"\"\n",
#                 "        \n",
#                 "        #TODO: Nothing to do for this method. Try it out and see how it works.\n",
#                 "        \n",
#                 "        mu = self.mean\n",
#                 "        sigma = self.stdev\n",
#                 "\n",
#                 "        min_range = min(self.data)\n",
#                 "        max_range = max(self.data)\n",
#                 "        \n",
#                 "         # calculates the interval between x values\n",
#                 "        interval = 1.0 * (max_range - min_range) / n_spaces\n",
#                 "\n",
#                 "        x = []\n",
#                 "        y = []\n",
#                 "        \n",
#                 "        # calculate the x values to visualize\n",
#                 "        for i in range(n_spaces):\n",
#                 "            tmp = min_range + interval*i\n",
#                 "            x.append(tmp)\n",
#                 "            y.append(self.pdf(tmp))\n",
#                 "\n",
#                 "        # make the plots\n",
#                 "        fig, axes = plt.subplots(2,sharex=True)\n",
#                 "        fig.subplots_adjust(hspace=.5)\n",
#                 "        axes[0].hist(self.data, density=True)\n",
#                 "        axes[0].set_title('Normed Histogram of Data')\n",
#                 "        axes[0].set_ylabel('Density')\n",
#                 "\n",
#                 "        axes[1].plot(x, y)\n",
#                 "        axes[1].set_title('Normal Distribution for \\n Sample Mean and Sample Standard Deviation')\n",
#                 "        axes[0].set_ylabel('Density')\n",
#                 "        plt.show()\n",
#                 "\n",
#                 "        return x, y"
#             ]
#         },
#         {
#             "cell_type": "code",
#             "execution_count": null,
#             "metadata": {
#
#             },
#             "outputs": [
#
#             ],
#             "source": [
#                 "# Unit tests to check your solution\n",
#                 "\n",
#                 "import unittest\n",
#                 "\n",
#                 "class TestGaussianClass(unittest.TestCase):\n",
#                 "    def setUp(self):\n",
#                 "        self.gaussian = Gaussian(25, 2)\n",
#                 "\n",
#                 "    def test_initialization(self): \n",
#                 "        self.assertEqual(self.gaussian.mean, 25, 'incorrect mean')\n",
#                 "        self.assertEqual(self.gaussian.stdev, 2, 'incorrect standard deviation')\n",
#                 "\n",
#                 "    def test_pdf(self):\n",
#                 "        self.assertEqual(round(self.gaussian.pdf(25), 5), 0.19947,\\\n",
#                 "         'pdf function does not give expected result') \n",
#                 "\n",
#                 "    def test_meancalculation(self):\n",
#                 "        self.gaussian.read_data_file('numbers.txt', True)\n",
#                 "        self.assertEqual(self.gaussian.calculate_mean(),\\\n",
#                 "         sum(self.gaussian.data) / float(len(self.gaussian.data)), 'calculated mean not as expected')\n",
#                 "\n",
#                 "    def test_stdevcalculation(self):\n",
#                 "        self.gaussian.read_data_file('numbers.txt', True)\n",
#                 "        self.assertEqual(round(self.gaussian.stdev, 2), 92.87, 'sample standard deviation incorrect')\n",
#                 "        self.gaussian.read_data_file('numbers.txt', False)\n",
#                 "        self.assertEqual(round(self.gaussian.stdev, 2), 88.55, 'population standard deviation incorrect')\n",
#                 "                \n",
#                 "tests = TestGaussianClass()\n",
#                 "\n",
#                 "tests_loaded = unittest.TestLoader().loadTestsFromModule(tests)\n",
#                 "\n",
#                 "unittest.TextTestRunner().run(tests_loaded)"
#             ]
#         }
#     ],
#     "metadata": {
#         "kernelspec": {
#             "display_name": "Python 3",
#             "language": "python",
#             "name": "python3"
#         },
#         "language_info": {
#             "codemirror_mode": {
#                 "name": "ipython",
#                 "version": 3
#             },
#             "file_extension": ".py",
#             "mimetype": "text/x-python",
#             "name": "python",
#             "nbconvert_exporter": "python",
#             "pygments_lexer": "ipython3",
#             "version": "3.9.1"
#         }
#     },
#     "nbformat": 4,
#     "nbformat_minor": 2
# }
