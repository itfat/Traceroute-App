import 'package:flutter/material.dart';

class Body extends StatelessWidget {
  const Body({ Key? key }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.lightGreen,
      child: Column(
        children:[
          buildInputField(),
          SizedBox(height:10),
          ElevatedButton(
              onPressed: () {
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
                enabledMouseCursor:
                    MouseCursor.defer, //used to construct ButtonStyle.mouseCursor
                disabledMouseCursor: MouseCursor
                    .uncontrolled, //used to construct ButtonStyle.mouseCursor
                visualDensity: VisualDensity(
                    horizontal: 0.0,
                    vertical: 0.0), //set the button's visual density
                tapTargetSize: MaterialTapTargetSize
                    .padded, // set the MaterialTapTarget size. can set to: values, padded and shrinkWrap properties
                animationDuration:
                    Duration(milliseconds: 100), //the buttons animations duration
                enableFeedback: true, //to set the feedback to true or false
                alignment: Alignment.center, //set the button's child Alignment
              ),
            ),
        ]
      ),
      
    );
  }
  TextFormField buildInputField() {
    return TextFormField(
      obscureText: true,
      // onSaved: (newValue) => password = newValue,
      onChanged: (value) {
        // if (value.isNotEmpty) {
        //   removeError(error: kPassNullError);
        // } else if (value.length >= 8) {
        //   removeError(error: kShortPassError);
        // }
        // password = value;

        return null;
      },
      validator: (value) {
        // if (value.isEmpty) {
        //   addError(error: kPassNullError);
        //   return "";
        // } else if (value.length < 8) {
        //   addError(error: kShortPassError);
        //   return "";
        // }
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