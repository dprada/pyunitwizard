import pyunitwizard as puw
import numpy as np

## from string

def test_convert_from_string_to_pint():  
    puw.configure.reset()
    puw.configure.load_library(['pint'])

    ureg = puw.forms.api_pint.ureg

    quantity = puw.convert('1 meter')
    assert quantity == ureg.Quantity(1, 'meter')

    quantity = puw.convert('1 meter', to_unit='cm')
    assert quantity == ureg.Quantity(100.0, 'centimeter')

    quantity = puw.convert('1 meter', to_type='unit')
    assert quantity == ureg.Unit('meter')

    quantity = puw.convert('1 meter', to_unit='cm', to_type='unit')
    assert quantity == ureg.Unit('centimeter')
   
def test_convert_from_string_to_string():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
   
    quantity = puw.convert('1 meter', to_unit='cm', to_form='string')
    assert quantity == '100.0 centimeter'

    quantity = puw.convert('1 meter', to_unit='cm', to_form='string', to_type='unit')
    assert quantity == 'centimeter'

    quantity = puw.convert('1 meter', to_type='value')
    assert quantity == 1

    quantity = puw.convert('1 meter', to_unit='cm', to_type='value')
    assert quantity == 100.0

    quantity = puw.convert('100 angstroms**3', to_form='string', to_type='unit')
    assert quantity == 'angstrom ** 3'
    
   
## to_pint

def test_convert_from_pint_to_pint():
    puw.configure.reset()
    puw.configure.load_library(['pint'])
    ureg = puw.forms.api_pint.ureg
    quantity = ureg.Quantity(2.5, 'nanometers/picoseconds')
    quantity = puw.convert(quantity, to_unit='angstroms/picoseconds')
    assert quantity == ureg.Quantity(25.0, 'angstroms/picoseconds')

## to_openmm_unit

def test_convert_from_pint_to_openmm_unit():
    puw.configure.reset()
    puw.configure.load_library(['pint','openmm.unit'])
    ureg = puw.forms.api_pint.ureg
    openmm_unit = puw.forms.api_openmm_unit.openmm_unit
    
    quantity = ureg.Quantity(2.5, 'nanometers/picoseconds')
    quantity = puw.convert(quantity, to_form='openmm.unit')
    assert quantity == 2.5 * openmm_unit.nanometer/openmm_unit.picosecond

    quantity = ureg.Quantity([2, 3, 7], 'meter')
    quantity = puw.convert(quantity, to_form='openmm.unit')
    assert quantity == np.array[2, 3, 7] * openmm_unit.meter

def test_to_openmm_unit_2():
    puw.configure.reset()
    puw.configure.load_library(['pint','openmm.unit'])
    ureg = puw.forms.api_pint.ureg
    openmm_unit = puw.forms.api_openmm_unit.openmm_unit
    q = ureg.Quantity([[0,0], [0,0]], 'nanometers/picoseconds')
    q = puw.convert(q, to_form='openmm.unit')
    q_true = [[0,0], [0,0]] * openmm_unit.nanometer/openmm_unit.picosecond
    assert np.all(q == q_true)

