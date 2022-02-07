from AppKit import NSWorkspace
from ApplicationServices import AXIsProcessTrusted
from Foundation import NSURL
import objc

# Workaround for ApplicationServices.AXIsProcessTrustedWithOptions
# since that fails with
# objc.internal_error: PyObjC: internal error in PyObjCFFI_ParseArguments at Modules/objc/libffi_support.m:3238: assertion failed: argbuf_cur <= argbuf_len
AS = objc.loadBundle('CoreServices', globals(),
                     '/System/Library/Frameworks/ApplicationServices.framework')
objc.loadBundleFunctions(AS, globals(),
                         [('AXIsProcessTrustedWithOptions', b'Z@')])
objc.loadBundleVariables(AS, globals(),
                         [('kAXTrustedCheckOptionPrompt', b'@')])

def isTrusted():
  return AXIsProcessTrusted()

def isTrustedWithPrompt():
  return AXIsProcessTrustedWithOptions({kAXTrustedCheckOptionPrompt: True})

def openAccessibilitySettings():
  url = NSURL.alloc().initWithString_("x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility")
  NSWorkspace.sharedWorkspace().openURL_(url)
