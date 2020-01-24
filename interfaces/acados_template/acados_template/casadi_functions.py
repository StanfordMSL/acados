#
# Copyright 2019 Gianluca Frison, Dimitris Kouzoupis, Robin Verschueren,
# Andrea Zanelli, Niels van Duijkeren, Jonathan Frey, Tommaso Sartor,
# Branimir Novoselnik, Rien Quirynen, Rezart Qelibari, Dang Doan,
# Jonas Koenemann, Yutao Chen, Tobias Schöls, Jonas Schlagenhauf, Moritz Diehl
#
# This file is part of acados.
#
# The 2-Clause BSD License
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.;
#

class AcadosSimModel():
    def __init__(self):
        # common
        self.x = None           #: CasADi variable describing the state of the system
        self.xdot = None        #: CasADi variable describing the derivative of the state wrt time
        self.u = None           #: CasADi variable describing the input of the system
        self.z = []             #: CasADi variable describing the algebraic variables of the DAE
        self.p = []             #: CasADi variable describing parameters of the DAE
        self.name = None        #: model name
        # dynamics
        self.f_impl_expr = None #: CasADi expression for the implicit dynamics :math:`F(\dot{x}, x, u, z) = 0`
        self.f_expl_expr = None #: CasADi expression for the explicit dynamics :math:`\dot{x} = f(x, u)`


class AcadosOcpModel( AcadosSimModel ):
    def __init__(self):
        # constraints
        self.con_h_expr   = None #: CasADi expression for the constraint
        self.con_phi_expr = None #: CasADi expression for the constraint
        self.con_r_expr   = None #: CasADi expression for the constraint
        self.con_phi_expr = None #: CasADi expression for the constraint
        self.con_r_in_phi = None
        # terminal
        self.con_h_expr_e   = None #: CasADi expression for the constraint
        self.con_r_expr_e   = None #: CasADi expression for the constraint
        self.con_phi_expr_e = None #: CasADi expression for the constraint
        self.con_r_in_phi_e = None
        # cost
        self.cost_y_expr = None     #: CasADi expression for the cost


def acados_sim_model_strip_casadi_symbolics(model):
    out = model
    if 'f_impl_expr' in out.keys():
        del out['f_impl_expr']
    if 'f_expl_expr' in out.keys():
        del out['f_expl_expr']
    if 'x' in out.keys():
        del out['x']
    if 'xdot' in out.keys():
        del out['xdot']
    if 'u' in out.keys():
        del out['u']
    if 'z' in out.keys():
        del out['z']
    if 'p' in out.keys():
        del out['p']
    return out


def acados_ocp_model_strip_casadi_symbolics(model):
    out = model
    if 'f_impl_expr' in out.keys():
        del out['f_impl_expr']
    if 'f_expl_expr' in out.keys():
        del out['f_expl_expr']
    if 'x' in out.keys():
        del out['x']
    if 'xdot' in out.keys():
        del out['xdot']
    if 'u' in out.keys():
        del out['u']
    if 'z' in out.keys():
        del out['z']
    if 'p' in out.keys():
        del out['p']
    # constraints
    if 'con_phi_expr' in out.keys():
        del out['con_phi_expr']
    if 'con_h_expr' in out.keys():
        del out['con_h_expr']
    if 'con_r_expr' in out.keys():
        del out['con_r_expr']
    if 'con_r_in_phi' in out.keys():
        del out['con_r_in_phi']
    # terminal
    if 'con_phi_expr_e' in out.keys():
        del out['con_phi_expr_e']
    if 'con_h_expr_e' in out.keys():
        del out['con_h_expr_e']
    if 'con_r_expr_e' in out.keys():
        del out['con_r_expr_e']
    if 'con_r_in_phi_e' in out.keys():
        del out['con_r_in_phi_e']
    # cost
    if 'cost_y_expr' in out.keys():
        del out['cost_y_expr']
    if 'cost_y_expr_e' in out.keys():
        del out['cost_y_expr_e']
    return out

