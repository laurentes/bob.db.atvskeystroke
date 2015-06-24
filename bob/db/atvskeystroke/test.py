#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""A few checks at the ATVS Keystroke database.
"""

import os, sys
import unittest
import bob.db.atvskeystroke

class ATVSKeystrokeDatabaseTest(unittest.TestCase):
  """Performs various tests on the Biosecurid database."""

  def test01_clients(self):
    db = bob.db.atvskeystroke.Database()
    self.assertEqual(len(db.groups()), 1)
    self.assertEqual(len(db.clients()), 63)
    self.assertEqual(len(db.clients(groups='eval')), 63)
    #self.assertEqual(len(db.clients(groups='impostorEval')), 63)
    self.assertEqual(len(db.models()), 63)
    self.assertEqual(len(db.models(groups='eval')), 63)


  def test02_objects(self):
    db = bob.db.atvskeystroke.Database()
    self.assertEqual(len(db.objects()), 1512)
    # A
    self.assertEqual(len(db.objects(protocol='A')), 1512)
    
    self.assertEqual(len(db.objects(protocol='A', groups='eval')), 1512)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='enrol')), 378)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe')), 1134)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', classes='client')), 378)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', classes='impostor')), 756)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1])), 18)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1], classes='client')), 6)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1], classes='impostor')), 12)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1,2])), 36)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1,2], classes='client')), 12)
    self.assertEqual(len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1,2], classes='impostor')), 24)






  def test03_driver_api(self):

    from bob.db.base.script.dbmanage import main
    self.assertEqual(main('atvskeystroke dumplist --self-test'.split()), 0)
    self.assertEqual(main('atvskeystroke checkfiles --self-test'.split()), 0)
    self.assertEqual(main('atvskeystroke reverse Genuine_1_1 --self-test'.split()), 0)
    self.assertEqual(main('atvskeystroke path 3011 --self-test'.split()), 0)

