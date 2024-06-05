from dataLoader import DataLoader
from RCS import RCS
from resultWriter import ResultWriter
from plotter import Plotter
import numpy as np

def main():
    url = "https://jenyay.net/uploads/Student/Modelling/task_rcs.csv"
    variant_number = 7
    
    loader = DataLoader(url)
    D, fmin, fmax = loader.parse_csv(variant_number)

    frequencies = np.linspace(fmin, fmax, num=500)
    rcs_calculator = RCS(D / 2)
    results = []
    for freq in frequencies:
        rcs = rcs_calculator.calculate_rcs(freq)
        results.append({"freq": freq, "lambda": 3e8 / freq, "rcs": rcs})

    writer = ResultWriter("rcs_results.xml")
    writer.write_to_xml(results)

    plotter = Plotter()
    plotter.plot_rcs_vs_frequency(results)

if __name__ == "__main__":
    main()
