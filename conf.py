# -*- coding: utf-8 -*-

# This Nikola conf.py file adds the "sister" nikolaBase directory to the
# collection of Python modules and then imports a "base" conf.py from the
# nikolaBase Python package.

# You can over-ride any of the nikolaBase configuration settings by simply
# changing their values in this file...

import os
import sys

sys.path.append(os.path.abspath("../nikolaBase"))

from nikolaBase.conf_base import *

EXTRA_PLUGINS_DIRS = [
  os.path.abspath("../nikolaBase/plugins")
]

EXTRA_THEMES_DIRS = [
  os.path.abspath("../nikolaBase/themes")
]

# Add any local changes here!

# Data about this site
BLOG_AUTHOR = "Stephen Gaito"
BLOG_TITLE = "diSimplicial approach to mathematical physics"
SITE_URL = "https://diSimplex.perceptisys.co.uk/"
BLOG_EMAIL = "stephen@perceptisys.co.uk"
BLOG_DESCRIPTION = "A diSimplicial approach to mathematical physics through computation."

# Uncomment the following line in any sub-sites which *are* blogs
#THIS_IS_A_BLOG_SITE = True
INDEX_DISPLAY_POST_COUNT = 15

# Uncomment the following line to make use of diSimplex's ServerSideIncludes
RENDER_DISIMPLEX_THEME_PARTIALS = True

DEPLOY_COMMANDS = {
  'default' : [
    'useKey stg',
    'rsync -av output/ stg@pi01:/home/plabs/nginx/diSimplex/html'
  ],
}

DEFAULT_LANG = "en"
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("/about",                                      "About"),
        ("/wiki",                                       "Wiki"),
        ("/blog",                                       "Blog"),
        ("/pictures/gallery",                           "Photos"),
        ("/refs",                                       "Refs"),
        ("/accounts/0Records/html/index.html",          "Accounts"),
        ("/notes",                                      "Notes"),
        ("https://disimplex.perceptisys.co.uk",         "diSimplex"),
        ("https://cTime.greyson-gaito.com/toDoSTG",     "ToDo"),
        ("https://cTime.greyson-gaito.com/timetracker", "Time"),
        ("/search",                                     "Search"),
    ),
}

CONTENT_FOOTER="""
<div class="wrapper">

  <h2 class="footer-heading">
    <a href="https://www.poetryfoundation.org/poems/47254/gerontion" target="_blank">
      A dull head among windy spaces
    </a>
  </h2>

  <div class="footer-col-wrapper">
    <div class="footer-col  footer-col-1">
      <ul class="contact-list">
        <li><a href="https://perceptisys.co.uk/" target="_blank">RealityLab</a></li>
        <li><a href="mailto:stephen@perceptisys.co.uk">stephen@perceptisys.co.uk</a></li>
        <li><a href="/poweredby">Powered By</a></li>
      </ul>
    </div>

    <div class="footer-col  footer-col-2">
      <ul class="contact-list">
        <li>
          <a href="https://github.com/stephenGaito" target="_blank">
            <span class="icon">
              <svg viewBox="0 0 16 16">
                <path fill="#828282" d="M7.999,0.431c-4.285,0-7.76,3.474-7.76,7.761 c0,3.428,2.223,6.337,5.307,7.363c0.388,0.071,0.53-0.168,0.53-0.374c0-0.184-0.007-0.672-0.01-1.32 c-2.159,0.469-2.614-1.04-2.614-1.04c-0.353-0.896-0.862-1.135-0.862-1.135c-0.705-0.481,0.053-0.472,0.053-0.472 c0.779,0.055,1.189,0.8,1.189,0.8c0.692,1.186,1.816,0.843,2.258,0.645c0.071-0.502,0.271-0.843,0.493-1.037 C4.86,11.425,3.049,10.76,3.049,7.786c0-0.847,0.302-1.54,0.799-2.082C3.768,5.507,3.501,4.718,3.924,3.65 c0,0,0.652-0.209,2.134,0.796C6.677,4.273,7.34,4.187,8,4.184c0.659,0.003,1.323,0.089,1.943,0.261 c1.482-1.004,2.132-0.796,2.132-0.796c0.423,1.068,0.157,1.857,0.077,2.054c0.497,0.542,0.798,1.235,0.798,2.082 c0,2.981-1.814,3.637-3.543,3.829c0.279,0.24,0.527,0.713,0.527,1.437c0,1.037-0.01,1.874-0.01,2.129 c0,0.208,0.14,0.449,0.534,0.373c3.081-1.028,5.302-3.935,5.302-7.362C15.76,3.906,12.285,0.431,7.999,0.431z"/>
              </svg>
            </span>

            <span class="username">stephenGaito</span>
          </a>
        </li>

        <li>
          <a href="https://git.perceptisys.co.uk/stg" target="_blank">
            <span class="icon">
              <img src="/images/gitea-32.png" width="16px" height="16px">
            </span>

            <span class="username">stg</span>
          </a>
        </li>

        <li>
          <a href="https://gitlab.freedesktop.org/stgaito" target="_blank">
            <span class="icon">
              <img src="/images/gitlab-freedesktop-fdo-logo.png" width="16px" height="16px">
            </span>

            <span class="username">stgaito</span>
          </a>
        </li>

        <li>
          <a href="https://twitter.com/StephenGaito" target="_blank">
            <span class="icon">
              <svg viewBox="0 0 16 16">
                <path fill="#828282" d="M15.969,3.058c-0.586,0.26-1.217,0.436-1.878,0.515c0.675-0.405,1.194-1.045,1.438-1.809
                c-0.632,0.375-1.332,0.647-2.076,0.793c-0.596-0.636-1.446-1.033-2.387-1.033c-1.806,0-3.27,1.464-3.27,3.27 c0,0.256,0.029,0.506,0.085,0.745C5.163,5.404,2.753,4.102,1.14,2.124C0.859,2.607,0.698,3.168,0.698,3.767 c0,1.134,0.577,2.135,1.455,2.722C1.616,6.472,1.112,6.325,0.671,6.08c0,0.014,0,0.027,0,0.041c0,1.584,1.127,2.906,2.623,3.206 C3.02,9.402,2.731,9.442,2.433,9.442c-0.211,0-0.416-0.021-0.615-0.059c0.416,1.299,1.624,2.245,3.055,2.271 c-1.119,0.877-2.529,1.4-4.061,1.4c-0.264,0-0.524-0.015-0.78-0.046c1.447,0.928,3.166,1.469,5.013,1.469 c6.015,0,9.304-4.983,9.304-9.304c0-0.142-0.003-0.283-0.009-0.423C14.976,4.29,15.531,3.714,15.969,3.058z"/>
              </svg>
            </span>

            <span class="username">StephenGaito</span>
          </a>
        </li>
      </ul>
    </div>

    <div class="footer-col  footer-col-3">
      <p class="text">A dull head provides a private place to explore the exposition of a mathematical theory of Reality.</p>
    </div>
  </div>

</div>
"""
