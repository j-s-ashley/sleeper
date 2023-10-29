ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP1()

      IMPLICIT NONE
      INCLUDE 'model_functions.inc'

      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_1 = -(MDL_EE*MDL_COMPLEXI)/3.000000D+00
      GC_2 = (2.000000D+00*MDL_EE*MDL_COMPLEXI)/3.000000D+00
      GC_363 = MDL_EE*MDL_COMPLEXI*MDL_I39A55
      GC_921 = -(MDL_CW*MDL_EE*MDL_COMPLEXI)/(2.000000D+00*(-1.000000D
     $ +00+MDL_SW)*MDL_SW*(1.000000D+00+MDL_SW))
      GC_922 = (MDL_CW*MDL_EE*MDL_COMPLEXI)/(2.000000D+00*(-1.000000D
     $ +00+MDL_SW)*MDL_SW*(1.000000D+00+MDL_SW))
      GC_923 = -(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_SW)/(3.000000D+00*(
     $ -1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
      GC_924 = (2.000000D+00*MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_SW)
     $ /(3.000000D+00*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
      GC_929 = (MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_I163A55*MDL_SW)/((
     $ -1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
      END
