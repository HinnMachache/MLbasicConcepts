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

    def read_file(self, file_name, sample=True):
        """
            Method to read data from a text file. Text file is expected to have numbers.
            After reading, the file, the mean and standard deviation are calculated.
        :param file_name:
                File_name thst contains the data
        :param sample:
                Determines whether samples read are data or population data
        :return:
                None
        """

        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(line)
                line = file.readline()
        file.close()

        self.data = data_list  # Update self.data with the data list
        self.mean = self.calculate_mean()  # Update self.mean with the mean of the data list
        self.stdev = self.calculate_stdev(sample)  # Update self.sdtdev with standard dev of the data list

    def plot_histogram(self):
        """
        Method to output a histogram of the instance variable data using
        matplotlib pyplot library
        :return:
            None
        """
        # TODO: Plot a histogram of the data_list using the matplotlib package.
        plt.plot(self.data)
        plt.title("Histogram of Data")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()

    def pdf(self, x):
        """
        Probability density function calculator for the gaussian distribution.
        Args:
            (float): point for calculating the probability density function
        Returns:
            float: probability density function output
        """
        # Calculate the probability density function of the Gaussian distribution
        mu = self.mean
        sigma = self.stdev
        return (1 / math.sqrt(2 * math.pi * sigma ** 2)) * (math.e ** (-((x - mu) ** 2) / (2 * sigma ** 2)))

    def plot_histogram_pdf(self, n_spaces=50):
        """
        Method to plot the normalized histogram of the data and a plot of the
        probability density function along the same range
        :param self:
                Object
        :param n_spaces:
                Number of data points
        :return:
                list: x values for the pdf plot
                list: y values for the pdf plot
        """
        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)

        # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces
        x = []
        y = []
        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval * i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2, sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')
        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y

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
