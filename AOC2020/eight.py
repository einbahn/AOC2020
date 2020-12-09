from aocd.models import Puzzle
from pprint import pprint as pp

class Instruction(object):
    def __init__(self, op, arg, acc=0, visited=False):
        self.op = op
        self.arg = arg
        self.acc_val = acc
        self.instruction_index = []
        self.instruction_ptr = []
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
    while ins_ptr < len(boot_code):
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


def swap(instruction):
    if instruction.op == 'nop':
        instruction.op = 'jmp'
    else:
        instruction.op = 'nop'

def handheld_halting_brute_force(instructions):
    from copy import deepcopy
    boot_code = []
    for i in instructions.split('\n'):
        op, arg = i.split(" ")
        boot_code.append(Instruction(op, int(arg)))
    nop_or_jmp = []
    for i, j in enumerate(boot_code):
        if j.op == 'nop' or j.op == 'jmp':
            nop_or_jmp.append(i)
    for i in nop_or_jmp:
        acc = 0
        ins_ptr = 0
        ins_cnt = 1
        found = True
        boot_code_copy = deepcopy(boot_code)
        swap(boot_code_copy[i])
        while ins_ptr < len(boot_code_copy):
            curr_ins = boot_code_copy[ins_ptr]
            if curr_ins.visited:
                curr_ins.instruction_index.append(ins_cnt)
                curr_ins.acc = acc
                found = False
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
                curr_ins.visited = True
                curr_ins.instruction_index.append(ins_cnt)
                curr_ins.acc = acc
                ins_ptr += curr_ins.arg
                ins_cnt += 1
        if found:
            return acc