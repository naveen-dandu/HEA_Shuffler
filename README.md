![CI](https://github.com/your-username/HEA_Shuffler/actions/workflows/ci.yml/badge.svg)
![CI](https://github.com/ndandu/HEA_Shuffler/actions/workflows/ci.yml/badge.svg)
[![CI](https://github.com/ndandu/HEA_Shuffler/actions/workflows/ci.yml/badge.svg)](https://github.com/ndandu/HEA_Shuffler/actions)

# HEA_Shuffler

**HEA_Shuffler** is a brute-force Monte Carlo atom substitution tool tailored for High-Entropy Alloy (HEA) simulations. It performs randomized substitution of atomic sites within a crystal structure and ranks configurations based on Short-Range Order (SRO) scoring.

## Features
- User-defined host and substituting atoms
- Random sampling via Monte Carlo
- SRO scoring using Voronoi nearest-neighbor method
- POSCAR outputs sorted by atomic species for VASP compatibility

## Quick Start

```bash
cd scripts
python HEA_Shuffler.py
```

## Example

```text
Enter the name of your POSCAR file (e.g., POSCAR): ../examples/POSCAR
Which atom do you want to substitute (e.g., Co)? Co
How many atoms do you want to substitute? [1 <= n <= 12] 8
Enter the substituting atom(s), separated by spaces (e.g., Mn Fe): Mn Fe
How many Monte Carlo trials to attempt? 10
```

## Outputs
- `POSCAR_trial_*.vasp`: Each configuration generated during sampling
- SRO Score printed for each trial

## License
MIT License
