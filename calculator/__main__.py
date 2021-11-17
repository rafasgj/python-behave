# This file is part of gerkin-by-example
#
# Copyright (C) 2021 Rafael Guterres Jeffman
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <https://www.gnu.org/licenses/>.

"""System implementation."""

from calculator.calculator import Calculator

def main():
    calculator = Calculator()
    calculator.add_input(int(input()))
    calculator.add_input(int(input()))
    print(f"X = {calculator.sum()}")

if __name__ == "__main__":
    main()
