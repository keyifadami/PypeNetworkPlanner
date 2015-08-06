
<h1> PypeNetworkPlanner</h1>

 <span>
     PypeNetworkPlanner is organized into 5 subdirectories. Each directory constitutes a module.
     Each module handles a different part of the project, the modules are:
 </span>
<p>
    <ul>
        <li>graph : this is the underlying data strucuture in which all the relevant data in the software is stored</li>
        <p></p>
        <li>gui : this handles all the graphical interface which the user, uses to interact with the graph</li>
        <p></p>
        <li>icons : this simply holds all the images and icons used in the software</li>
        <p></p>
        <li>solver : solver, although currently empty, is meant to hold all files used to solve simulations (an interface for the graph and solver will have to be constructed)</li>
        <p></p>
        <li>utils(utilities) : this is a general purpose module to hold functions and classes that do not fit will into the above catagories but are still necessary (e.g. math functions)</li>
    </ul>
</p>

<hr>

<h3> TODO </h3>
<ul>
    <li><span>   The thing I was trying to do with the project when I decided to step away, was the connecting of the graph to the TabPanels </span>
    <span>   The main problem in doing this for me was my lack of knowledge in the wxPython ListCtrl widget</span>
    <span>   To complete this you will need to build an interface between the graph and the ListCtrl widget</span></li>
    <p></p>
    <li><span>   undo/redo is completely unimplemented in the current version. It will need to be implemented by storing the state of the graph at each change.</span></li>

</ul>

<hr>
<h3> KNOWN BUGS </h3>

<ul>
    <li>The drawing on zoomin / zoomout will disappear untill another mode is selected</li>
    <li>The same is true when new frames are introduced over the frame containing DrawingPanel </li>
</ul>
