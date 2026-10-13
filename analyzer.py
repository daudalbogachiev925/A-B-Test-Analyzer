from dataclasses import dataclass
from scipy import stats
import numpy as np

@dataclass
class ABResult:
    control_conv: int
    control_total: int
    variant_conv: int
    variant_total: int

    @property
    def p_control(self): return self.control_conv / self.control_total
    @property
    def p_variant(self): return self.variant_conv / self.variant_total
    @property
    def uplift(self): return (self.p_variant - self.p_control) / self.p_control
    @property
    def z_score(self):
        p = (self.control_conv + self.variant_conv) / (self.control_total + self.variant_total)
        se = np.sqrt(p * (1 - p) * (1/self.control_total + 1/self.variant_total))
        return (self.p_variant - self.p_control) / se if se > 0 else 0
    @property
    def p_value(self):
        return 2 * (1 - stats.norm.cdf(abs(self.z_score)))
    @property
    def significant(self):
        return self.p_value < 0.05
