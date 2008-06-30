from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand

class _Wedge(_HPGLCommand):
   '''Abstract wedge.'''
   def __init__(self, radius, startangle, sweepangle, chordangle = 22.5):
      self.radius = Scalable(radius)
      self.startangle = startangle
      self.sweepangle = sweepangle
      self.chordangle = chordangle

   def __str__(self):
      return '%s%.4f,%.4f,%.4f,%.4f%s' % (self._name, self.radius, self.startangle,
                                      self.sweepangle, self.chordangle, 
                                      self.terminator)