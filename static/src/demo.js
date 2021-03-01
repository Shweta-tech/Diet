import React from "react";
import { withStyles } from "@material-ui/core/styles";
import MuiExpansionPanel from "@material-ui/core/ExpansionPanel";
import MuiExpansionPanelSummary from "@material-ui/core/ExpansionPanelSummary";
import MuiExpansionPanelDetails from "@material-ui/core/ExpansionPanelDetails";
import Typography from "@material-ui/core/Typography";
import { makeData } from "./Utils";
import ReactTable from "react-table";
import "react-table/react-table.css";
import Map from "./mapview.js";

const ExpansionPanel = withStyles({
  root: {
    border: "1px solid rgba(0,0,0,.125)",
    boxShadow: "none",
    "&:not(:last-child)": {
      borderBottom: 0
    },
    "&:before": {
      display: "none"
    }
  },
  expanded: {
    margin: "auto"
  }
})(MuiExpansionPanel);

const ExpansionPanelSummary = withStyles({
  root: {
    backgroundColor: "rgba(0,0,0,.03)",
    borderBottom: "1px solid rgba(0,0,0,.125)",
    marginBottom: -1,
    minHeight: 56,
    "&$expanded": {
      minHeight: 56
    }
  },
  content: {
    "&$expanded": {
      margin: "12px 0"
    }
  },
  expanded: {}
})(props => <MuiExpansionPanelSummary {...props} />);

ExpansionPanelSummary.muiName = "ExpansionPanelSummary";

const ExpansionPanelDetails = withStyles(theme => ({
  root: {
    padding: theme.spacing.unit * 2
  }
}))(MuiExpansionPanelDetails);

class CustomizedExpansionPanel extends React.Component {
  constructor() {
    super();
    this.state = {
      data: makeData(),
      expanded: "panel1"
    };
    this.child = React.createRef();
  }
  handleChange = panel => (event, expanded) => {
    this.setState({
      expanded: expanded ? panel : false
    });
  };
  onClick = () => {
    this.child.current.getAlert();
  };

  render() {
    const { expanded, data } = this.state;
    var tableHeight;
    if (!this.state.expanded) {
      tableHeight = 800;
    } else {
      tableHeight = 800;
    }
    return <Map />;
  }
}

export default CustomizedExpansionPanel;
