import unittest
from main import Cylinder

class TestCylinder(unittest.TestCase):
    cyl = Cylinder(10,10)
    def test_volume_should_pass(self):
        self.assertEquals(self.cyl.getVolume(),3140)
    
    def test_volume_should_fail(self):
        self.assertEquals(self.cyl.getVolume(),2000)
    
    def test_surface_area_should_pass(self):
        self.assertEquals(self.cyl.getSurfaceArea(),1256)
    
    def test_surface_area_should_fail(self):
        self.assertEquals(self.cyl.getSurfaceArea(),2000)

if __name__ == "__main__":
    unittest.main()