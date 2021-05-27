import argparse
import csv
import os


def row_stats(input_file, output_file, start_index=6):
    """[create row stats for data file]

    Args:
        input_file ([string]): [the path of the input file]
        output_file ([string]): [the path of the output file]
        start_index ([int]): [the first numerical column index], default index is 6.
        ['id', 'study_id', 'sample_id', 'biome', 'exptype', 'version', 'feature1', ....]
    """
    with open(input_file, 'r') as f:
        with open(output_file, 'w') as f_out:
            reader = csv.reader(f, delimiter="\t")
            writer = csv.writer(f_out, delimiter="\t")
            header = next(reader)
            writer.writerow(header[:start_index] +['cnt', 'sum'])
            for row in reader:
                sum_ = sum([float(i) for i in row[start_index:]])  # the row sum
                cnt = sum([float(i) > 0 for i in row[start_index:]])  # the number of non zero values in one row
                writer.writerow(row[:start_index] + [cnt, sum_])


def col_sum(input_file, output_file, start_index=6):
    """[create col sum file] eg:
    id   sum
    0    s1
    1    s2
    Args:
        input_file ([string]): [the path of the input file]
        output_file ([string]): [the path of the output file]
        start_index ([int]): [the first numerical column index], default index is 6.
        ['id', 'study_id', 'sample_id', 'biome', 'exptype', 'version', 'feature1', ....]
    """
    with open(input_file, 'r') as f_in:
        with open(output_file, 'w') as f_out:
            reader = csv.reader(f_in, delimiter="\t")
            writer = csv.writer(f_out, delimiter="\t")
            header = next(reader)
            writer.writerow(['feature', 'sum'])
            features = header[start_index:]
            res = [0] * len(features)
            for row in reader:
                for i in range(len(features)):
                    res[i] += float(row[i+start_index])
            # write res to output file
            for i in range(len(features)):
                writer.writerow([features[i], res[i]])


def main(input_file, output_dir):
    row_stats_file = os.path.join(output_dir, 'row_stats.tsv')
    col_stats_file = os.path.join(output_dir, 'col_stats.tsv')
    row_stats(input_file, row_stats_file)
    col_sum(input_file, col_stats_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Creating stats for input file')
    parser.add_argument('input_file_path',
                        type=str,
                        help='the path to the input file')
    parser.add_argument('--output_dir_path',
                        type=str,
                        help='the path to the output file directory, '
                             'if not specified, will create a new dir called "data"')
    args = parser.parse_args()
    input_file_path = args.input_file_path
    ouput_data_dir = args.output_dir_path
    if ouput_data_dir is None:
        ouput_data_dir = 'data'
        os.makedirs(ouput_data_dir, exist_ok=True)
    main(input_file_path, ouput_data_dir)