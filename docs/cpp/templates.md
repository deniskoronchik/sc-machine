
Templates is a very powerful mechanism to work with semantic network (graph). You can search and generate any constructions using templates.
There are list of available classes to work with templates:
* `ScTemplate` - class that represents template in C++ code;
* `ScTemplateParams` - parameters that contains values of variables in template. This class usually used when you generate construction by template;
* `ScTemplateSearchResult` - contains result of search by template (list of found constructions);
* `ScTemplateSearchResultItem` - represents on search result item;
* `ScTemplateGenResult` - represent result of generation by template.

## ScTemplate
Class to work with templates in c++. Before reading this paragraph you need to read common [information about types](el_types.md).

Let use `f` symbols for fixed (constant) parameter of template. Let use `a` symbol for a assignable (variable) parameter of template. There are possible 3 types of simple templates:

* `f_a_a` - template to find all outgoing edges from a specified sc-element;
* `f_a_f` - template to find all edges between two specified sc-elements;
* `a_a_f` - template to find all ingoing edges to a specified sc-element.

### Create template

#### Manual

Use `ScTemplateBuilder` to create `ScTemplate` directly from a code.

`ScTemplateBuilder::Triple` - this function adds triple construction into template. There are some examples of using this function to produce simple templates:

<table>
  <tr>
    <th>Template</th>
    <th>Description</th>
  </tr>

  <tr>
    <td>f_a_a</td>
    <td>
      <strong>Graphical representation</strong>
      <br/><scg src="../../images/templates/template_triple_f_a_a_example.gwf"></scg>
      <br/><strong>Equal C++ code</strong>
      <br/>
<pre><code class="cpp hljs">
ScTemplateBuilder builder;
builder.Triple(
  param1,
  ScType::EdgeAccessVarPosPerm,
  ScType::NodeVar
);
</code></pre>
      <br/>This triple template using to traverse output edges from specified sc-element.
      <ul>
       <li><code>param1</code> - is a known <code>ScAddr</code> of source sc-element. <i><b>Use <code>ScAddr</code> of any sc-element</b></i></li>
       <li>second parameter - <code>ScType</code> of required outgoing edge. <i><b>Use only non constant edge types</b></i></li>
       <li>third parameter - <code>ScType</code> of required target element. <i><b>Use any non constant type</b></i></li>
      </ul>
    </td>
  </tr>

  <tr>
    <td>f_a_f</td>
    <td><strong>Graphical representation</strong>
    <br/><scg src="../../images/templates/template_triple_f_a_f_example.gwf"></scg>
    <br/><strong>Equal C++ code</strong>
    <br/>
<pre><code class="cpp hljs">
ScTemplateBuilder builder;
builder.Triple(
  param1,
  ScType::EdgeAccessVarPosPerm,
  param3
);
</code></pre>
      <br/>This triple template using to find edge between two sc-elements.
      <ul>
       <li><code>param1</code> - is a known <code>ScAddr</code> of source sc-element. <i><b>Use <code>ScAddr</code> of any sc-element</b></i></li>
       <li>second parameter - <code>ScType</code> of required edge. <i><b>Use only non constant edge types</b></i></li>
       <li><code>param3</code> - is a known <code>ScAddr</code> of target sc-element. <i><b>Use <code>ScAddr</code> of any sc-element</b></i></li>
      </ul>

    </td>
  </tr>

  <tr>
    <td>a_a_f</td>
    <td><strong>Graphical representation</strong>
    <br/><scg src="../../images/templates/template_triple_a_a_f_example.gwf"></scg>
    <br/><strong>Equal C++ code</strong>
    <br/>
<pre><code class="cpp hljs">
ScTemplateBuilder builder;
builder.Triple(
  ScType::NodeVar,
  ScType::EdgeAccessVarPosPerm,
  param3
);
</code></pre>
      <br/>This triple template using to traverse ingoing edges to specified sc-element.
      <ul>
        <li>first parameter - <code>ScType</code> of required source element. <i><b>Use any non constant type</b></i></li>
        <li>second parameter - <code>ScType</code> of required ingoing edge. <i><b>Use only non constant edge types</b></i></li>
        <li><code>param3</code> - is a known <code>ScAddr</code> of target sc-element. <i><b>Use <code>ScAddr</code> of any sc-element</b></i></li>
      </ul>
    </td>
  </tr>
</table>

It is possible to assign text name for elements in `ScTemplate`. Use `>>` operator for parameters in `ScTemplateBuilder::Triple` function. 
These named sc-elements can be used in next triples instead of `ScAddr` for a known sc-elements. Search engine will substitue found sc-element as known.
That allow to link a lot of triples into one big template. Example:

```cpp
ScTemplateBuilder builder;
builder.Triple(
  addr,
  ScType::EdgeAccessVarPosPerm >> "_edge",
  ScType::NodeVar >> "_node");

builder.Triple(
  ScType::NodeVar >> "_attr",
  ScType::EdgeAccessVarPosPerm,
  "_edge");

builder.Triple(
  other_addr,
  ScType::EdgeAccessVarPosPerm,
  "_node");

ScTemplatePtr templ = builder.Template();
```

С++ code above describes this template:
<scg src="../../images/templates/template_named_param_example.gwf"></scg>

The same template can be done with `ScTemplateBuilder::TripleWithRelation` function. This fuction call equals to two calls of `Triple` functions.

```cpp
ScTemplateBuilder builder;

/**
 * builder.Triple(
 * addr,
 * ScType::EdgeAccessVarPosPerm >> "_edge",
 * ScType::NodeVar >> "_node");
 *
 * builder.Triple(
 * ScType::NodeVar >> "_attr",
 * ScType::EdgeAccessVarPosPerm,
 * "_edge");
 *   
 * Replace these two calls with one
 */

builder.TripleWithRelation(
  addr,
  ScType::EdgeAccessVarPosPerm,
  ScType::NodeVar >> "_node",
  ScType::EdgeAccessVarPosPerm,
  ScType::NodeVar >> "_attr");

builder.Triple(
  other_addr,
  ScType::EdgeAccessVarPosPerm,
  "_node");

ScTemplatePtr templ = builder.Template();
```

#### With SCs-text

Another option to create template - is to use [SCs-text](../other/scs.md). Use `ScTemplateSCsBuilder` class for that.

```cpp
std::string const scs_text = "addr _-> _attr:: _node;; _node _<- other_addr;;";

ScTemplateBuilderSCs builder(scs_text);
ScTemplatePtr template = builder.Template();
```

!!! note
    All system identifiers will be resolved as fixed (constant) sc-elements (`addr` and `other_addr` in exampe above)

#### From SC-memory



## Search

Search algorithm trying to find all possible variants of specified construction. It use any constants (available `ScAddr`'s from parameters to find equal constructions in sc-memory).



## Search in construction

Do the same as [Search](#search), but check if all elements of found constructions are in a specified set.

Example:

```cpp
ScTemplate templ; 
templ.Triple(
  anyAddr >> "_anyAddr",
  ScType::EdgeAccessVarPosPerm >> "_edge",
  ScType::NodeVar >> "_trgAddr");
  
ctx.HelperSearchTemplateInStruct(templ, anyStructAddr, result)
```

## Generate
