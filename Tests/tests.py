import unittest
import MyFileInfoLib.MyFileInfoLibClass as f
class UnitTest ( unittest.TestCase ):
    def testOldDate ( self ):
        a = f.MyfileInfoLibClass ( "D:\Test\Test.txt", "D:\Test\Test2.txt", "D:\Test\Test3.txt", "D:\Test\Test4.txt" )
        self.assertEqual ( a.GetTheOldestFileName (  ), "D:\\Test\\Test.txt" ) 
    def testNewDate ( self ):
        b = f.MyfileInfoLibClass ( "D:\Test\Test.txt", "D:\Test\Test2.txt", "D:\Test\Test3.txt", "D:\Test\Test4.txt" )
        self.assertEqual (  b.GetTheNewestFileName (  ), "D:\\Test\\Test4.txt" )
    def testMaxSize ( self ):
        c = f.MyfileInfoLibClass ( "D:\Test\Test.txt", "D:\Test\Test2.txt", "D:\Test\Test3.txt", "D:\Test\Test4.txt" )
        self.assertEqual ( c.GetTheBiggestFileName (  ), "D:\Test\Test.txt" )
    def testMinSize ( self ):
        d = f.MyfileInfoLibClass ( "D:\Test\Test.txt", "D:\Test\Test2.txt", "D:\Test\Test3.txt", "D:\Test\Test4.txt" )
        self.assertEqual ( d.GetTheSmallestFileName (), "D:\\Test\\Test4.txt" )

if __name__ == "__main__":
    unittest.main()