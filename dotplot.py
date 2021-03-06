import sys
from argument_parser import ArgumentParser
from drawer import Drawer
from plotter import Plotter
from sequence import Sequence


class Dotplot(object):
    def __init__(self, sequences, plotter_args=None, drawer_args=None):
        self.sequences = [Sequence.from_fasta_file(sequences.file1),
                          Sequence.from_fasta_file(sequences.file2)]
        self.plotter = Plotter(plotter_args)
        self.drawer = Drawer(drawer_args)

    def make_plot(self):
        self.plot = self.plotter.plot(self.sequences)

    def draw(self, plot=None):
        if not plot:
            plot = self.plot
        self.drawer.draw(plot)


if __name__ == '__main__':
    args = ArgumentParser().parse(sys.argv)
    dotplot = Dotplot(args.sequences, args.plotter, args.drawer)
    dotplot.make_plot()
    dotplot.draw()
