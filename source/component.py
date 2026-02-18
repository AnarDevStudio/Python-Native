class Component:
    def __init__(self, **props):
        self.props = props  

    def onClick(self):
        handler = self.props.get("onClick")  
        if callable(handler):
            handler()  #
        else:
            print("onClick triggered")

    def onContextMenu(self):
        print("onContextMenu triggered")

    def onDoubleClick(self):
        print("onDoubleClick triggered")

    def onMouseDown(self):
        print("onMouseDown triggered")

    def onMouseEnter(self):
        print("onMouseEnter triggered")

    def onMouseLeave(self):
        print("onMouseLeave triggered")

    def onMouseMove(self):
        print("onMouseMove triggered")

    def onMouseOut(self):
        print("onMouseOut triggered")

    def onMouseOver(self):
        print("onMouseOver triggered")

    def onMouseUp(self):
        print("onMouseUp triggered")

    # Keyboard Events
    def onKeyDown(self):
        print("onKeyDown triggered")

    def onKeyPress(self):
        print("onKeyPress triggered")

    def onKeyUp(self):
        print("onKeyUp triggered")

    # Focus Events
    def onFocus(self):
        print("onFocus triggered")

    def onBlur(self):
        print("onBlur triggered")

    # Form Events
    def onChange(self):
        print("onChange triggered")

    def onInput(self):
        print("onInput triggered")

    def onSubmit(self):
        print("onSubmit triggered")

    def onInvalid(self):
        print("onInvalid triggered")

    def onReset(self):
        print("onReset triggered")

    # Composition Events
    def onCompositionStart(self):
        print("onCompositionStart triggered")

    def onCompositionUpdate(self):
        print("onCompositionUpdate triggered")

    def onCompositionEnd(self):
        print("onCompositionEnd triggered")

    # Clipboard Events
    def onCopy(self):
        print("onCopy triggered")

    def onCut(self):
        print("onCut triggered")

    def onPaste(self):
        print("onPaste triggered")

    # Drag & Drop Events
    def onDrag(self):
        print("onDrag triggered")

    def onDragEnd(self):
        print("onDragEnd triggered")

    def onDragEnter(self):
        print("onDragEnter triggered")

    def onDragExit(self):
        print("onDragExit triggered")

    def onDragLeave(self):
        print("onDragLeave triggered")

    def onDragOver(self):
        print("onDragOver triggered")

    def onDragStart(self):
        print("onDragStart triggered")

    def onDrop(self):
        print("onDrop triggered")

    # Pointer Events
    def onPointerDown(self):
        print("onPointerDown triggered")

    def onPointerMove(self):
        print("onPointerMove triggered")

    def onPointerUp(self):
        print("onPointerUp triggered")

    def onPointerCancel(self):
        print("onPointerCancel triggered")

    def onGotPointerCapture(self):
        print("onGotPointerCapture triggered")

    def onLostPointerCapture(self):
        print("onLostPointerCapture triggered")

    def onPointerEnter(self):
        print("onPointerEnter triggered")

    def onPointerLeave(self):
        print("onPointerLeave triggered")

    def onPointerOver(self):
        print("onPointerOver triggered")

    def onPointerOut(self):
        print("onPointerOut triggered")

    # Touch Events
    def onTouchStart(self):
        print("onTouchStart triggered")

    def onTouchMove(self):
        print("onTouchMove triggered")

    def onTouchEnd(self):
        print("onTouchEnd triggered")

    def onTouchCancel(self):
        print("onTouchCancel triggered")

    # Media Events
    def onAbort(self):
        print("onAbort triggered")

    def onCanPlay(self):
        print("onCanPlay triggered")

    def onCanPlayThrough(self):
        print("onCanPlayThrough triggered")

    def onDurationChange(self):
        print("onDurationChange triggered")

    def onEmptied(self):
        print("onEmptied triggered")

    def onEncrypted(self):
        print("onEncrypted triggered")

    def onEnded(self):
        print("onEnded triggered")

    def onError(self):
        print("onError triggered")

    def onLoadedData(self):
        print("onLoadedData triggered")

    def onLoadedMetadata(self):
        print("onLoadedMetadata triggered")

    def onLoadStart(self):
        print("onLoadStart triggered")

    def onPause(self):
        print("onPause triggered")

    def onPlay(self):
        print("onPlay triggered")

    def onPlaying(self):
        print("onPlaying triggered")

    def onProgress(self):
        print("onProgress triggered")

    def onRateChange(self):
        print("onRateChange triggered")

    def onSeeked(self):
        print("onSeeked triggered")

    def onSeeking(self):
        print("onSeeking triggered")

    def onStalled(self):
        print("onStalled triggered")

    def onSuspend(self):
        print("onSuspend triggered")

    def onTimeUpdate(self):
        print("onTimeUpdate triggered")

    def onVolumeChange(self):
        print("onVolumeChange triggered")

    def onWaiting(self):
        print("onWaiting triggered")

    # Image Events
    def onLoad(self):
        print("onLoad triggered")

    # Animation / Transition Events
    def onAnimationStart(self):
        print("onAnimationStart triggered")

    def onAnimationEnd(self):
        print("onAnimationEnd triggered")

    def onAnimationIteration(self):
        print("onAnimationIteration triggered")

    def onTransitionEnd(self):
        print("onTransitionEnd triggered")

    # Misc / Scroll / Wheel
    def onScroll(self):
        print("onScroll triggered")

    def onWheel(self):
        print("onWheel triggered")

    def onToggle(self):
        print("onToggle triggered")

class Return:
    def __init__(self, *children, **props):
        print("returned")

