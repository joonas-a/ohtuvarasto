import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ylitaytto_ei_mahdollinen(self):
        self.varasto.lisaa_varastoon(20)
        
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_negatiivinen_ottaminen_ei_mahdollinen(self):

        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0.0)

    def test_liian_suuri_maara_ottaa_kaiken_mitä_on(self):
        self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(self.varasto.ota_varastosta(100), 0)

    def test_string_tulostuu_oikein(self):
        teksti = self.varasto.__str__()

        self.assertAlmostEqual("saldo = 0, vielä tilaa 10", teksti)

class TestVarasto2(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(-10, -10)
    
    def test_konstruktori_korjaa_virheellisen_tilavuuden(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_konstruktori_korjaa_virheellisen_saldon(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivinen_lisaaminen_ei_mahdollinen(self):
        lisays = self.varasto.lisaa_varastoon(-1)

        self.assertEqual(lisays, None)

class TestVarasto3(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(5, 10)

    def test_suurempi_saldo_kuin_tilavuus_toimii_oikein(self):
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)