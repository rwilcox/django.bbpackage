Introduction
==========================

Hi, I'm [Ryan Wilcox](http://flavors.me/rwilcox). You may know me as a [long time freelancer](http://www.wilcoxd.com), or as the person behind [@bbedit_hints](http://www.twitter.com/bbedit_hints).

I've been involved with a number of Django projects over the years, and have collected disparate tools for writing Python (and Django) in BBEdit up in this package.

Installation
============

    $ cd Library/Application\ Support/BBEdit/
    $ mkdir Packages # if it doesn't already exists
    $ cd Packages
    $ git clone https://github.com/rwilcox/django.bbpackage.git

And restart BBEdit.

Contributing
======================

Please feel free to contribute. However, there is something to keep in mind: BBEdit for some reason doesn't like the uncompiled versions of some Applescripts.

Plus, having BBEdit compile an Applescript every time is much slower than compiling it once.

To avoid this, I've created a ApplescriptSources folder. Modify the .applescript file here, then save a compiled version in the Scripts/git folder.

At some point I'll write a shell script or Makefile to automate this process, or figure out what's wrong...

License
================

Public domain

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


Thanks
===================================

A great number of clippings were taken from Greg Newman's [Django Clippings for BBEdit](https://github.com/gregnewman/django-bbedit).
