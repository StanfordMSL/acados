
#ifndef INTERFACES_ACADOS_CPP_OCP_NLP_OCP_NLP_H_
#define INTERFACES_ACADOS_CPP_OCP_NLP_OCP_NLP_H_

#include <map>
#include <string>
#include <vector>

#include "acados_cpp/options.hpp"

#include "casadi/casadi.hpp"

namespace acados {

class ocp_nlp {
    typedef unsigned int uint;
 
 public:
    ocp_nlp(std::vector<uint> nx, std::vector<uint> nu, std::vector<uint> nbx, std::vector<uint> ng,
            std::vector<uint> nh, std::vector<uint> ns);

    void solve();

    std::vector<std::string> fields = {"lbx", "ubx", "lbu", "ubu", "C", "D", "lg", "ug", "lh", "uh"};

    void set_field(std::string field, uint stage);

    void set_model(const casadi::Function& f, std::map<std::string, option_t *> options = {});

    void set_constraint(const casadi::Function& h);

};

}  // namespace acados

#endif  // INTERFACES_ACADOS_CPP_OCP_NLP_OCP_NLP_H_
