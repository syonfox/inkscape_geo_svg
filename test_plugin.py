#!/usr/bin/env python
import inkex

class TestExtension(inkex.EffectExtension):
    def effect(self):
        inkex.debug("TestExtension is running!")

if __name__ == "__main__":
    TestExtension().run()
