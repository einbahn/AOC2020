from aocd.models import Puzzle


class Instruction(object):
    def __init__(self, op, arg, acc=0, visited=False):
        self.op = op
        self.arg = arg
        self.acc_val = acc
        self.instruction_index = []
        self.visited = visited

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)


def handheld_halting(instructions):
    acc = 0
    boot_code = []
    for i in instructions.split('\n'):
        op, arg = i.split(" ")
        boot_code.append(Instruction(op, int(arg)))
    ins_ptr = 0
    ins_cnt = 1
    while True:
        assert 0 <= ins_ptr <= len(boot_code)
        curr_ins = boot_code[ins_ptr]
        if curr_ins.visited:
            curr_ins.instruction_index.append(ins_cnt)
            curr_ins.acc = acc
            break
        if curr_ins.op == 'nop':
            curr_ins.instruction_index.append(ins_cnt)
            curr_ins.visited = True
            curr_ins.acc = acc
            ins_ptr += 1
            ins_cnt += 1
        elif curr_ins.op == 'acc':
            acc += curr_ins.arg
            curr_ins.acc = acc
            curr_ins.instruction_index.append(ins_cnt)
            curr_ins.visited = True
            ins_ptr += 1
            ins_cnt += 1
        elif curr_ins.op == 'jmp':
            curr_ins.instruction_index.append(ins_cnt)
            curr_ins.acc = acc
            ins_ptr += curr_ins.arg
            ins_cnt += 1
    return acc

if __name__ == '__main__':
    puzzle = Puzzle(year=2020, day=8)
    print("part one: {}".format(handheld_halting(puzzle.input_data)))
