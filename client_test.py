import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    expected1 = ('ABC', 120.48, 121.2, (120.48 + 121.2)/2)
    self.assertTupleEqual(getDataPoint(quotes[0]), expected1)

    expected2 = ('DEF', 117.87, 121.68, (117.87 + 121.68)/2)
    self.assertTupleEqual(getDataPoint(quotes[1]), expected2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    expected1 = ('ABC', 120.48, 119.2, (120.48 + 119.2)/2)
    self.assertTupleEqual(getDataPoint(quotes[0]), expected1)

    expected2 = ('DEF', 117.87, 121.68, (117.87 + 121.68)/2)
    self.assertTupleEqual(getDataPoint(quotes[1]), expected2)

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_regular(self):
    self.assertEqual(getRatio(15.0, 2.5), 6)

  def test_getRatio_priceAZero(self):
    self.assertEqual(getRatio(0, 2.5), 0)

  def test_getRation_priceBZero(self):
    self.assertIsNone(getRatio(15, 0))



if __name__ == '__main__':
    unittest.main()
