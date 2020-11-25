
import abstract_importer as imp
import structure as st
import trajectory as tr


class SamplePath:
    """
    Aggregates all the informations about the trajectories, the real structure of the sampled net and variables
    cardinalites.
    Has the task of creating the objects that will contain the mentioned data.

    :_importer: the Importer objects that will import ad process data
    :trajectories: the Trajectory object that will contain all the concatenated trajectories
    :structure: the Structure Object that will contain all the structurral infos about the net
    :_total_variables_count: the number of variables in the net

    """
    def __init__(self, importer: imp.AbstractImporter):
        """
        Parameters:
            :importer: the Importer objects that will import ad process data
        """
        self._importer = importer
        self._trajectories = None
        self._structure = None
        self._total_variables_count = None
        self._importer.import_data()

    def build_trajectories(self):
        """
        Builds the Trajectory object that will contain all the trajectories.
        Clears all the unused dataframes in Importer Object

        Parameters:
            :void
        Returns:
            :void
        """
        #self._importer.import_data()
        self._trajectories = \
            tr.Trajectory(self._importer.build_list_of_samples_array(self._importer.concatenated_samples),
                          len(self._importer.sorter) + 1)
        #self.trajectories.append(trajectory)
        self._importer.clear_concatenated_frame()

    def build_structure(self):
        """
        Builds the Structure object that aggregates all the infos about the net.
        Parameters:
            :void
        Returns:
            :void
        """
        if self._importer.sorter != self._importer.variables.iloc[:, 0].to_list():
            raise RuntimeError("The Dataset columns order have to match the order of labels in the variables Frame!")

        self._total_variables_count = len(self._importer.sorter)
        labels = self._importer.variables.iloc[:, 0].to_list()
        indxs = self._importer.variables.index.to_numpy()
        vals = self._importer.variables.iloc[:, 1].to_numpy()
        edges = list(self._importer.structure.to_records(index=False))
        self._structure = st.Structure(labels, indxs, vals, edges,
                                       self._total_variables_count)

    @property
    def trajectories(self) -> tr.Trajectory:
        return self._trajectories

    @property
    def structure(self) -> st.Structure:
        return self._structure

    @property
    def total_variables_count(self):
        return self._total_variables_count





