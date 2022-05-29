---
marp:true
---
---

# Advanced Graph

---

# Comparisons of Common Graph Packages

- Seaborn
- Matplotlib
- Plotly
- bokeh


---

# Comparisons of Common Graph Packages

**Matplotlib** is a popular plotting package that is being continuously developed. It offers numerous rendering backends and uses a verbose syntax, giving plots a high degree of flexibility and customizability.

**seaborn** is a Python plotting library built on top of Matplotlib. It allows for a concise but limited approach to quickly visualize data sets with better-looking style defaults than Matplotlib.

**Plotly** is a mostly open-source data analytics and visualization tool (with some closed-source products and services). It creates interactive charts for web browsers and supports multiple languages, such as Python, Julia, R, and MATLAB.

***Bokeh*** appears to have a much smaller core team, which means that their product is leaner and meaner, with a fairly narrow focus of what the module *can* and *cannot* do. On the other hand, the lack of manpower means that they are often slow to bring new features to the code (I am *still* waiting for a good table component for data) and some bugs can linger for longer that expected. It is Python-centric and deeply integrated with the language, although secondary R, Julia and Scala bindings exist with various states of feature parity. There are also a host of other third party modules, part of the [HoloViz](https://holoviz.org/) framework (like HoloViews, GeoViews and Datashader), which attempt to extend Bokeh (and Matplotlib!) with a higher level interface. Unfortunately, there is a large degree of overlap between features, making their use somewhat confusing.


source: [Matplotlib vs. seaborn vs. Plotly vs. MATLAB vs. ggplot2 vs. pandas - Ritza Articles](https://ritza.co/articles/matplotlib-vs-seaborn-vs-plotly-vs-MATLAB-vs-ggplot2-vs-pandas/)


---

# install packages


```
pip install seaborn --user
```


```
pip install matplotlib --user
```

---

# Gallery

[Example gallery — seaborn 0.11.2 documentation (pydata.org)](http://seaborn.pydata.org/examples/index.html)

---

# Scientific Publications

Peebles, D., & Ali, N. (2009). [Differences in comprehensibility between three-variable bar and line graphs](http://csjarchive.cogsci.rpi.edu/Proceedings/2009/papers/648/paper648.pdf).  *Proceedings of the Thirty-First Annual Conference of the Cognitive Science Society* , 2938–2943. Retrieved from http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.412.4953

Peebles, D., & Ali, N. (2015). [Expert interpretation of bar and line graphs: The role of graphicacy in reducing the effect of graph format](http://peebles%2C%20d.%2C%20%26%20ali%2C%20n.%20%282015%29.%20expert%20interpretation%20of%20bar%20and%20line%20graphs:%20the%20role%20of%20graphicacy%20in%20reducing%20the%20effect%20of%20graph%20format.xn--%20frontiers%20in%20psychology%2C%206%28oct%29%2C%20111-lt38a.%20https//doi.org/10.3389/fpsyg.2015.01673).  *Frontiers in Psychology* ,  *6* (OCT), 1–11. [https://doi.org/10.3389/fpsyg.2015.01673](https://doi.org/10.3389/fpsyg.2015.01673)
