class Materialize(object):
    def __init__(self):
        self.node_type = 'Materialize'

    def __str__(self):
        return 'Materialize'


class Aggregate(object):
    def __init__(self, strategy, keys, input, output, avg_row_len):
        self.node_type = 'Aggregate'
        self.strategy = strategy
        self.group_keys = keys
        self.input = input
        self.output = output
        self.avg_row_len = avg_row_len


    def __str__(self):
        return 'Aggregate ON: ' + ','.join(self.group_keys)


class Sort(object):
    def __init__(self, sort_keys, input, output, avg_row_len):
        self.sort_keys = sort_keys
        self.node_type = 'Sort'
        self.input = input
        self.output = output
        self.avg_row_len = avg_row_len


    def __str__(self):
        return 'Sort by: ' + ','.join(self.sort_keys)


class Hash(object):
    def __init__(self, input, output, avg_row_len):
        self.node_type = 'Hash'
        self.input = input
        self.output = output
        self.avg_row_len = avg_row_len


    def __str__(self):
        return 'Hash'


class Join(object):
    def __init__(self, node_type, condition_seq, input, output, avg_row_len):
        self.node_type = node_type
        self.condition = condition_seq
        self.input = input
        self.output = output
        self.avg_row_len = avg_row_len


    def __str__(self):
        return self.node_type + ' ON ' + ','.join([str(i) for i in self.condition])


class Scan(object):
    def __init__(self, node_type, condition_seq_filter, condition_seq_index, relation_name, index_name, input, output, avg_row_len):
        self.node_type = node_type
        self.condition_filter = condition_seq_filter
        self.condition_index = condition_seq_index
        self.relation_name = relation_name
        self.index_name = index_name
        self.input = input
        self.output = output
        self.avg_row_len = avg_row_len


    def __str__(self):
        return self.node_type + ' ON ' + ','.join([str(i) for i in self.condition_filter]) + '; ' + ','.join(
            [str(i) for i in self.condition_index])


class BitmapCombine(object):
    def __init__(self, operator, input, output, avg_row_len):
        self.node_type = operator
        self.input = input
        self.output = output
        self.avg_row_len = avg_row_len


    def __str__(self):
        return self.node_type


class Result(object):
    def __init__(self):
        self.node_type = 'Result'

    def __str__(self):
        return 'Result'
