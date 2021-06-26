import 'package:flutter/material.dart';
import 'package:string_validator/string_validator.dart';

class Body extends StatefulWidget {
  const Body({Key? key}) : super(key: key);

  @override
  _BodyState createState() => _BodyState();
}

class _BodyState extends State<Body> {
  final _formKey = GlobalKey<FormState>();
  var dest;
  @override
  Widget build(BuildContext context) {
    return Form(
        key: _formKey,
        child: Container(
          color: Colors.lightGreen,
          child: Column(children: [
            buildInputField(),
            SizedBox(height: 10),
            ElevatedButton(
              onPressed: () {
                if (_formKey.currentState!.validate()) {
                  // If the form is valid, display a snackbar. In the real world,
                  // you'd often call a server or save the information in a database.
                  ScaffoldMessenger.of(context)
                      .showSnackBar(SnackBar(content: Text('Processing Data')));
                }
              },
              child: Text(
                'Trace',
                style: TextStyle(color: Colors.white),
              ),
              style: ElevatedButton.styleFrom(
                primary: Colors.black, //button's fill color
                shadowColor: Colors.grey, //specify the button's elevation color
                elevation: 7.0, //buttons Material shadow
                minimumSize: Size(150,
                    40), //specify the button's first: width and second: height
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(
                        35.0)), // set the buttons shape. Make its birders rounded etc
                enabledMouseCursor: MouseCursor
                    .defer, //used to construct ButtonStyle.mouseCursor
                disabledMouseCursor: MouseCursor
                    .uncontrolled, //used to construct ButtonStyle.mouseCursor
                visualDensity: VisualDensity(
                    horizontal: 0.0,
                    vertical: 0.0), //set the button's visual density
                tapTargetSize: MaterialTapTargetSize
                    .padded, // set the MaterialTapTarget size. can set to: values, padded and shrinkWrap properties
                animationDuration: Duration(
                    milliseconds: 100), //the buttons animations duration
                enableFeedback: true, //to set the feedback to true or false
                alignment: Alignment.center, //set the button's child Alignment
              ),
            ),
          ]),
        ));
  }

  TextFormField buildInputField() {
    return TextFormField(
      onChanged: (value) {
        dest = value;
      },
      validator: (value) {
        if (value == null || value.isEmpty) {
          print(isIP(value.toString()));
          print(isFQDN(value.toString()));
          return "Input field can not be empty";
        }
        else if(!(isIP(value.toString()) || isFQDN(value.toString()))){
          return "Please enter valid input";

        }
        return null;
      },
      decoration: InputDecoration(
        focusColor: Colors.lightGreen,
        hoverColor: Colors.black,
        border: InputBorder.none,
        hintText: "Enter your IP/HostName",
        hintStyle: TextStyle(color: Colors.grey),
        filled: true,
        fillColor: Colors.white,
        floatingLabelBehavior: FloatingLabelBehavior.always,
      ),
    );
  }
}
