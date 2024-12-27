import unittest
import demo

class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calculate = demo.Calculate()

    def tearDown(self):
        print("This is a teardown method executes after each test")

    def test_add(self): 
        self.assertEqual(self.calculate.add(4,5),9)

    def test_sub(self):
        self.assertEqual(self.calculate.sub(10,5),5)
    
    @unittest.skipIf(True,"Skipping because the condition is true")
    def test_mul(self):
        self.assertEqual(self.calculate.mul(4,5),20)

    def test_div(self):
        self.assertEqual(self.calculate.div(40,5),8)
        with self.assertRaises(ValueError):
            self.calculate.div(10,0)            

if __name__ == '__main__':
    unittest.main()        