import qt
from slicer.ScriptedLoadableModule import *


class RTLManager:
    """
    RTL support manager. May be used to activate/deactivate RTL support
    """

    def enableRTL(self):
        """
        Enable RTL support for the entire application
        """
        try:
            # Set application layout direction to RTL
            app = qt.QApplication.instance()
            app.setLayoutDirection(qt.Qt.RightToLeft)

            # Apply global stylesheet for RTL support
            app.setStyleSheet("""
                * {
                    font-family: Arial;
                    text-align: right;
                }
                QPushButton, QToolButton {
                    text-align: center;
                }
                QLabel, QLineEdit, QComboBox, QCheckBox, QRadioButton {
                    text-align: right;
                }
                QMenuBar::item {
                    padding: 4px 8px;
                }
                QMenu::item {
                    padding: 4px 25px 4px 20px;
                }
            """)

            # Apply RTL to all existing widgets
            for widget in app.topLevelWidgets():
                self.applyRTLToWidget(widget)

                # Apply RTL text alignment to all buttons and labels
                self.applyRTLTextAlignment(widget)

                # Flip icon positions
                self.flipIconPositions(widget)

            # Force update all widgets
            app.processEvents()

        except Exception as e:
            # Show error message if something goes wrong
            print("An unexpected error happened when activating RTL support")
            import traceback
            error_msg = f"{str(e)}\n\n{traceback.format_exc()}"
            print(error_msg)

    def flipIconPositions(self, widget):
        """
        Apply RTL and right alignment to all widgets
        """
        try:
            if not widget:
                return

            # Apply RTL direction to all widgets
            if hasattr(widget, 'setLayoutDirection'):
                widget.setLayoutDirection(qt.Qt.RightToLeft)

                # Apply right alignment for text-based widgets
                if hasattr(widget, 'setAlignment'):
                    widget.setAlignment(qt.Qt.AlignRight | qt.Qt.AlignVCenter)

            # Apply styles based on widget type
            if isinstance(widget, (qt.QPushButton, qt.QToolButton)):
                # Set icon to the right of text
                if not widget.icon().isNull() and widget.text():
                    widget.setToolButtonStyle(qt.Qt.ToolButtonTextBesideIcon)

                # Apply center alignment style
                widget.setStyleSheet("""
                    QPushButton, QToolButton {
                        text-align: center;
                        padding: 4px 8px;
                        stop: 0 #d9d9d9, stop: 1 #f6f7fa);
                    }
                    QPushButton::icon, QToolButton::icon {
                        padding-left: 5px;
                        padding-right: 0px;
                        background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                      stop: 0 #d9d9d9, stop: 1 #f6f7fa);
                    }
                """)

            # Handle QPushButton (standard buttons)
            elif isinstance(widget, qt.QPushButton):
                try:
                    icon = widget.icon()
                    text = widget.text()

                    # Create a centered button with icon and text
                    centered_btn = RTLCenteredButton()

                    # Store original widget for signal connections
                    original_widget = widget

                    # Copy properties from original button
                    centered_btn.setObjectName(original_widget.objectName())
                    centered_btn.setEnabled(original_widget.isEnabled())
                    centered_btn.setVisible(original_widget.isVisible())
                    centered_btn.setToolTip(original_widget.toolTip())
                    centered_btn.setCheckable(original_widget.isCheckable())
                    centered_btn.setChecked(original_widget.isChecked())
                    centered_btn.setAutoDefault(original_widget.autoDefault())
                    centered_btn.setDefault(original_widget.isDefault())

                    # Set text and icon with center alignment
                    centered_btn.setText(text)
                    if not icon.isNull():
                        centered_btn.setIcon(icon)

                    # Set parent after setting up the button
                    if original_widget.parent():
                        centered_btn.setParent(original_widget.parent())

                    # Copy geometry if possible
                    if original_widget.parent() and original_widget.parent().layout():
                        # Replace in layout if it's in a layout
                        layout = original_widget.parent().layout()
                        index = layout.indexOf(original_widget)
                        if index >= 0:
                            # Store the layout stretch factors
                            row, col, rowSpan, colSpan = layout.getItemPosition(index)

                            # Create a container widget to center the button
                            container = qt.QWidget()
                            container_layout = qt.QHBoxLayout(container)
                            container_layout.setContentsMargins(0, 0, 0, 0)
                            container_layout.addStretch()
                            container_layout.addWidget(centered_btn)
                            container_layout.addStretch()

                            # Replace the original widget with the container
                            layout.removeWidget(original_widget)
                            layout.addWidget(container, row, col, rowSpan, colSpan)
                            original_widget.setParent(None)
                            original_widget.deleteLater()
                    else:
                        # Just set the same geometry
                        centered_btn.setGeometry(original_widget.geometry())
                        original_widget.setParent(None)
                        original_widget.deleteLater()

                    # Connect signals using lambda to maintain reference
                    if hasattr(original_widget, 'clicked'):
                        centered_btn.clicked.connect(original_widget.clicked.emit)
                    if hasattr(original_widget, 'toggled'):
                        centered_btn.toggled.connect(original_widget.toggled.emit)
                    if hasattr(original_widget, 'pressed'):
                        centered_btn.pressed.connect(original_widget.pressed.emit)
                    if hasattr(original_widget, 'released'):
                        centered_btn.released.connect(original_widget.released.emit)

                    # Apply center alignment styles
                    centered_btn.setStyleSheet("""
                        RTLCenteredButton {
                            text-align: center;
                            padding: 5px 15px;
                            spacing: 5px;
                            margin: 0px;
                            border: none;
                            background-color: transparent;
                        }
                        RTLCenteredButton::icon {
                            padding: 0px;
                            margin: 0px;
                            width: 16px;
                            height: 16px;
                        }
                    """)

                    # Force update
                    centered_btn.update()
                    centered_btn.updateGeometry()

                    # Return the new button
                    widget = centered_btn

                except Exception as e:
                    print(f"Error processing button {widget.objectName()}: {str(e)}")

            # Handle QAction (menu items and toolbar actions)
            elif isinstance(widget, qt.QAction):
                if widget.text():
                    # Create a custom widget for the action
                    action_widget = qt.QWidget()
                    layout = qt.QHBoxLayout(action_widget)
                    layout.setContentsMargins(4, 2, 4, 2)
                    layout.setSpacing(8)

                    # Add icon if exists
                    if not widget.icon().isNull():
                        icon_label = qt.QLabel()
                        icon_label.setPixmap(widget.icon().pixmap(16, 16))
                        layout.addWidget(icon_label)

                    # Add text
                    text_label = qt.QLabel(widget.text())
                    layout.addWidget(text_label)

                    # Add stretch to push content to the right
                    layout.addStretch()

                    # Set the widget as the action's default widget
                    widget.setDefaultWidget(action_widget)

                    # Apply RTL styles
                    action_widget.setStyleSheet("""
                        QLabel {
                            text-align: right;
                            padding: 2px 4px;
                        }
                    """)

            # Handle QLabel with both icon and text
            elif isinstance(widget, qt.QLabel):
                if widget.pixmap() and widget.text():
                    # For labels with both icon and text, create a custom layout
                    layout = qt.QHBoxLayout()
                    layout.setContentsMargins(0, 0, 0, 0)
                    layout.setSpacing(4)

                    # Add pixmap and text in reverse order
                    icon_label = qt.QLabel()
                    icon_label.setPixmap(widget.pixmap())

                    text_label = qt.QLabel(widget.text())
                    text_label.setAlignment(qt.Qt.AlignRight | qt.Qt.AlignVCenter)

                    layout.addWidget(icon_label)
                    layout.addWidget(text_label)

                    # Clear the original content and set the new layout
                    widget.clear()
                    widget.setLayout(layout)

            # Handle QComboBox items
            elif isinstance(widget, qt.QComboBox):
                # Set RTL direction for the combobox
                widget.setLayoutDirection(qt.Qt.RightToLeft)

                # Apply custom style to ensure proper RTL display
                widget.setStyleSheet("""
                    QComboBox {
                        padding-right: 5px;
                        text-align: right;
                    }
                    QComboBox QAbstractItemView {
                        text-align: right;
                    }
                """)

            # Recursively process all child widgets
            for child in widget.children():
                if isinstance(child, qt.QWidget):
                    self.flipIconPositions(child)

        except Exception as e:
            # Log the error but don't crash
            import traceback
            print(f"Error in flipIconPositions: {str(e)}\n{traceback.format_exc()}")

    def applyRTLTextAlignment(self, widget):
        """
        Apply RTL text alignment to all supported widgets
        """
        try:
            # Apply to buttons
            if isinstance(widget, qt.QPushButton) and not isinstance(widget, RTLCenteredButton):
                # Replace with our custom button
                button = RTLCenteredButton(widget.text())
                button.setParent(widget.parent())
                button.setGeometry(widget.geometry())
                button.setVisible(widget.isVisible())
                button.setEnabled(widget.isEnabled())
                button.setToolTip(widget.toolTip)
                button.clicked.connect(widget.click)
                widget.deleteLater()
                return button

            # Apply to labels
            elif isinstance(widget, qt.QLabel):
                widget.setAlignment(qt.Qt.AlignRight | qt.Qt.AlignVCenter | qt.Qt.AlignAbsolute)
                widget.setIndent(5)

            # Apply to line edits
            elif isinstance(widget, qt.QLineEdit):
                widget.setAlignment(qt.Qt.AlignRight | qt.Qt.AlignVCenter)
                widget.setLayoutDirection(qt.Qt.RightToLeft)
                widget.setStyleSheet("""
                    QLineEdit {
                        text-align: right;
                        padding-right: 5px;
                    }
                """)

            # Apply to text edits
            elif isinstance(widget, (qt.QTextEdit, qt.QPlainTextEdit)):
                widget.setAlignment(qt.Qt.AlignRight)
                widget.document().setDefaultTextOption(qt.QTextOption(qt.Qt.AlignRight | qt.Qt.AlignVCenter))

            # Apply to combo boxes
            elif isinstance(widget, qt.QComboBox):
                widget.setLayoutDirection(qt.Qt.RightToLeft)
                widget.setStyleSheet("""
                    QComboBox {
                        text-align: right;
                        padding-right: 5px;
                    }
                    QComboBox QAbstractItemView {
                        text-align: right;
                    }
                """)

            # Apply to checkboxes and radio buttons
            elif isinstance(widget, (qt.QCheckBox, qt.QRadioButton)):
                widget.setLayoutDirection(qt.Qt.RightToLeft)
                widget.setStyleSheet("""
                    QCheckBox, QRadioButton {
                        spacing: 5px;
                    }
                """)

            # Apply to group boxes
            elif isinstance(widget, qt.QGroupBox):
                widget.setLayoutDirection(qt.Qt.RightToLeft)

            # Apply to tab widgets
            elif isinstance(widget, qt.QTabWidget):
                widget.setLayoutDirection(qt.Qt.RightToLeft)
                widget.setStyleSheet("""
                    QTabBar::tab {
                        padding: 5px 10px;
                    }
                """)

            # Force update the widget
            widget.update()

            # Apply to all children recursively
            for child in widget.children():
                self.applyRTLTextAlignment(child)

        except Exception as e:
            # Silently ignore any errors to prevent crashing the application
            pass

    def applyRTLToWidget(self, widget):
        """
        Recursively apply RTL to a widget and all its children
        """
        try:
            if widget is None:
                return

            # Skip widgets that are already processed
            # if hasattr(widget, '_rtl_processed'):
            #     return

            # Mark as processed
            # widget._rtl_processed = True

            # Set layout direction
            if hasattr(widget, 'layoutDirection'):
                widget.setLayoutDirection(qt.Qt.RightToLeft)

            # Special handling for C++ widgets
            widget_class = widget.metaObject().className()

            # Handle C++ widgets with specific class names
            if 'ctkPushButton' in widget_class or 'qMRMLNodeComboBox' in widget_class or 'qMRMLSliderWidget' in widget_class:
                # Apply RTL styles to C++ widgets
                current_style = widget.styleSheet() or ""
                widget.setStyleSheet(current_style + """
                    * {
                        text-align: right;
                        font-family: Arial;
                    }
                    QPushButton, QToolButton {
                        text-align: center;
                    }
                    QLabel, QLineEdit, QComboBox, QCheckBox, QRadioButton {
                        text-align: right;
                    }
                """)

                # Force update
                widget.update()
                widget.updateGeometry()

            # Apply to all children
            for child in widget.children():
                if isinstance(child, qt.QWidget):
                    self.applyRTLToWidget(child)

        except Exception as e:
            # Silently ignore any errors to prevent crashing the application
            pass



class RTLCenteredButton(qt.QPushButton):
    """A custom QPushButton with centered text in RTL mode"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI()

    def setupUI(self):
        # Set RTL direction
        self.setLayoutDirection(qt.Qt.RightToLeft)

        # Apply custom style for centered text and icon
        self.setStyleSheet("""
            RTLCenteredButton {
                text-align: center;
                padding: 5px 15px;
                spacing: 5px;
                margin: 0px;
                border: none;
                background-color: transparent;
            }
            RTLCenteredButton:focus {
                outline: none;
            }
            RTLCenteredButton::icon {
                padding: 0px;
                margin: 0px;
                width: 16px;
                height: 16px;
            }
            }
        """)

        # Set center alignment
        self.setProperty("class", "centered-button")

        # Create a layout for the button content
        self.layout = qt.QHBoxLayout(self)
        self.layout.setContentsMargins(6, 2, 6, 2)
        self.layout.setSpacing(5)

        # Add stretch to center the content
        self.layout.addStretch()

        # Add icon and text widgets
        self.iconLabel = qt.QLabel()
        self.textLabel = qt.QLabel()
        self.textLabel.setAlignment(qt.Qt.AlignCenter)

        # Add widgets to layout
        self.layout.addWidget(self.iconLabel)
        self.layout.addWidget(self.textLabel)

        # Add stretch to center the content
        self.layout.addStretch()

        # Hide by default, will be shown when set
        self.iconLabel.hide()
        self.textLabel.hide()

    def setText(self, text):
        """Override setText to handle custom text display"""
        if hasattr(self, 'textLabel'):
            self.textLabel.setText(text)
            self.textLabel.setVisible(bool(text))
        else:
            super().setText(text)

    def setIcon(self, icon):
        """Override setIcon to handle custom icon display"""
        if hasattr(self, 'iconLabel'):
            if icon and not icon.isNull():
                self.iconLabel.setPixmap(icon.pixmap(16, 16))
                self.iconLabel.show()
            else:
                self.iconLabel.hide()
        else:
            super().setIcon(icon)

    def paintEvent(self, event):
        # Call parent paint event
        super().paintEvent(event)

        # Create a painter for this button
        painter = qt.QStylePainter(self)

        # Get the style options
        option = qt.QStyleOptionButton()
        self.initStyleOption(option)

        # Draw the button text in the center
        textRect = self.style().subElementRect(qt.QStyle.SE_PushButtonContents, option, self)
        alignment = qt.Qt.AlignCenter | qt.Qt.TextShowMnemonic | qt.Qt.TextWordWrap

        # Draw the text
        painter.drawText(textRect, alignment, self.text())

        # Draw the focus frame if needed
        if self.hasFocus():
            option = qt.QStyleOptionFocusRect()
            option.initFrom(self)
            option.backgroundColor = self.palette().color(qt.QPalette.Background)
            self.style().drawPrimitive(qt.QStyle.PE_FrameFocusRect, option, painter, self)
