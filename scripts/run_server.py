import os
import sys

package_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(package_dir)

from finding_chart.server import app as application

if __name__ == "__main__":
    application.run(debug=True)
