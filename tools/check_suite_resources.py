'''
Usage: 

load a python3 environment (e.g. xp65/analysis3), then:

python check_suite_resources.py

Then enter your cylc-run dir when prompted (or add it as an argument on the python script call)
 
'''

import sys, glob, pandas # argparse, 


def lines_that_contain(string, fp):
    list_of_list = [line.rstrip('\n').replace(" ", "").split(':') for line in fp if string in line]
    flat_list = [item for sublist in list_of_list for item in sublist]
    return flat_list

def compute_total_resources(resources_list):
    df = pandas.DataFrame(resources_list, columns=['name', 'value'])
    df['value'] = df['value'].astype(float)
    df = df.dropna()
    return df

def main():
    """
    Print all matching lines (print them lazily, as we find them)
    """

    try: 
        suite_run_dir = sys.argv[1]
        print(f'checking {suite_run_dir}')
    except:
        suite_run_dir = input('Enter suite name: ')

    files = glob.glob(suite_run_dir + '/log/**/NN/job.out', recursive=True)
#    files = glob.glob(suite_run_dir + '/log/job/20200102T0000Z/**/NN/job.out', recursive=True)
    service_units = []
    for fl in files:

        with open(fl, "r") as fp:
            su = lines_that_contain("Service Units", fp)
            print(fl,su)
            service_units.append(su)
    r_su = compute_total_resources(service_units)
    print(f"SU used in {suite_run_dir}: {r_su['value'].sum()}")
    # print(r_su['value'].sum())

    return None

if __name__ == "__main__":
    """
    Environment:
    module use /g/data/xp65/public/modules
    module load conda/analysis3
    """
    main()

