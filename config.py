#!/usr/bin/env python3.11

def load_repos():
    repos = {
        "GhostBSD_Unstable": ("http://pkg.ghostbsd.org/unstable/${ABI}/latest", "http://pkg.ghostbsd.org/unstable/${ABI}/base"),
        "GhostBSD_CA": ("https://pkg.ca.ghostbsd.org/stable/${ABI}/latest", "https://pkg.ca.ghostbsd.org/stable/${ABI}/base"),
        "GhostBSD": ("https://pkg.ghostbsd.org/stable/${ABI}/latest", "https://pkg.ghostbsd.org/stable/${ABI}/base"),
        "GhostBSD_FR": ("https://pkg.fr.ghostbsd.org/stable/${ABI}/latest", "https://pkg.fr.ghostbsd.org/stable/${ABI}/base"),
        "GhostBSD_NO": ("http://pkg.no.ghostbsd.org/stable/${ABI}/latest", "http://pkg.no.ghostbsd.org/stable/${ABI}/base"),
        "GhostBSD_ZA": ("https://pkg.za.ghostbsd.org/stable/${ABI}/latest", "https://pkg.za.ghostbsd.org/stable/${ABI}/base")
    }
    return repos

